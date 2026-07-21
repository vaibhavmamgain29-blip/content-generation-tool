// Content Studio — frontend logic.
// Streams responses from the FastAPI backend using fetch + ReadableStream.

const $ = (sel) => document.querySelector(sel);
const API_BASE =
  import.meta.env.VITE_API_URL ||
  "https://content-generation-tool.onrender.com";

const els = {
  form: $("#gen-form"),
  prompt: $("#prompt"),
  temperature: $("#temperature"),
  tempVal: $("#temp-val"),
  maxTokens: $("#max-tokens"),
  submitBtn: $("#submit-btn"),
  stopBtn: $("#stop-btn"),
  clearBtn: $("#clear-btn"),
  copyBtn: $("#copy-btn"),
  output: $("#output"),
  errorBanner: $("#error-banner"),
  statusPill: $("#status-pill"),
};

const PRESETS = {
  blog:
    "Write a detailed blog outline for a post titled 'The Rise of Edge AI'. Include an intro hook, 5 H2 sections with bullet points, and a conclusion.",

  tagline:
    "Generate 10 punchy product taglines for a sustainable coffee brand called 'Terra Bean'. Keep each under 8 words.",

  email:
    "Write a friendly cold outreach email to a startup CTO introducing our AI code-review tool. Keep it under 150 words, end with a soft CTA.",

  recipe:
    "Write a 30-minute weeknight pasta recipe with pantry staples. Include ingredients, step-by-step instructions, and a pro tip.",
};

let controller = null;

// -----------------------------------------------------------------------------
// Backend Health
// -----------------------------------------------------------------------------

async function checkHealth() {
  setStatus("unknown", "Checking...");

  try {
    const res = await fetch(`${API_BASE}/api/health`);

    if (!res.ok) throw new Error();

    const data = await res.json();

    if (data.llm_configured) {
      setStatus("ok", `Backend ready · ${data.model}`);
    } else {
      setStatus("bad", "LLM not configured");
    }
  } catch {
    setStatus("bad", "Backend unreachable");
  }
}

function setStatus(kind, text) {
  const pill = els.statusPill;

  pill.classList.remove("pill--ok", "pill--bad", "pill--unknown");
  pill.classList.add(`pill--${kind}`);

  pill.querySelector(".pill-text").textContent = text;
}

// -----------------------------------------------------------------------------
// Streaming
// -----------------------------------------------------------------------------

async function streamGenerate(payload) {
  controller = new AbortController();

  let outputText = "";

  setOutput(outputText);

  const cursor = mountCursor();

  const res = await fetch(`${API_BASE}/api/generate`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
    signal: controller.signal,
  });

  if (!res.ok) {
    let detail = `HTTP ${res.status}`;

    try {
      const err = await res.json();
      detail = err.detail || detail;
    } catch {}

    throw new Error(detail);
  }

  const reader = res.body.getReader();
  const decoder = new TextDecoder();

  let buffer = "";

  while (true) {
    const { value, done } = await reader.read();

    if (done) break;

    buffer += decoder.decode(value, { stream: true });

    let idx;

    while ((idx = buffer.indexOf("\n\n")) !== -1) {
      const frame = buffer.slice(0, idx);

      buffer = buffer.slice(idx + 2);

      handleFrame(frame, (token) => {
        outputText += token;
        setOutput(outputText, cursor);
      });
    }
  }

  return outputText;
}

function handleFrame(frame, onToken) {
  const lines = frame.split("\n");

  let data = "";

  for (const line of lines) {
    if (line.startsWith("data:")) {
      data += line.slice(5).trim();
    }
  }

  if (!data) return;

  let payload;

  try {
    payload = JSON.parse(data);
  } catch {
    return;
  }

  switch (payload.type) {
    case "token":
      onToken(payload.content);
      break;

    case "error":
      throw new Error(payload.content);

    case "done":
      break;
  }
}

function mountCursor() {
  const cursor = document.createElement("span");

  cursor.className = "cursor";

  els.output.appendChild(cursor);

  return cursor;
}

function setOutput(text, cursor) {
  els.output.textContent = text;

  if (cursor) {
    els.output.appendChild(cursor);
  }
}

// -----------------------------------------------------------------------------
// UI
// -----------------------------------------------------------------------------

function setLoading(isLoading) {
  els.submitBtn.classList.toggle("is-loading", isLoading);

  els.submitBtn.disabled = isLoading;

  els.stopBtn.disabled = !isLoading;
}

function showError(message) {
  els.errorBanner.textContent = message;
  els.errorBanner.hidden = false;
}

function clearError() {
  els.errorBanner.hidden = true;
  els.errorBanner.textContent = "";
}

// -----------------------------------------------------------------------------
// Events
// -----------------------------------------------------------------------------

els.form.addEventListener("submit", async (e) => {
  e.preventDefault();

  clearError();

  const prompt = els.prompt.value.trim();

  if (!prompt) return;

  // Client-side validation
  if (prompt.length > 50000) {
    showError("Prompt exceeds the maximum allowed length (50,000 characters).");
    return;
  }

  const payload = {
    prompt,
    temperature: parseFloat(els.temperature.value),
    max_tokens: parseInt(els.maxTokens.value, 10),
  };

  setLoading(true);

  els.copyBtn.disabled = true;

  try {
    const text = await streamGenerate(payload);

    if (text) {
      els.copyBtn.disabled = false;
    }
  } catch (err) {
    if (err.name !== "AbortError") {
      showError(err.message || "Generation failed.");
    }
  } finally {
    setLoading(false);
    controller = null;
  }
});

els.stopBtn.addEventListener("click", () => {
  if (controller) {
    controller.abort();
  }
});

els.clearBtn.addEventListener("click", () => {
  els.prompt.value = "";

  els.output.innerHTML =
    '<div class="output-empty muted">Your generated content will appear here, streaming token by token.</div>';

  els.copyBtn.disabled = true;

  clearError();
});

els.copyBtn.addEventListener("click", async () => {
  const text = els.output.textContent.trim();

  if (!text) return;

  try {
    await navigator.clipboard.writeText(text);

    els.copyBtn.textContent = "Copied!";

    setTimeout(() => {
      els.copyBtn.textContent = "Copy";
    }, 1500);
  } catch {}
});

els.temperature.addEventListener("input", () => {
  els.tempVal.textContent = els.temperature.value;
});

document.querySelectorAll(".chip").forEach((chip) => {
  chip.addEventListener("click", () => {
    const preset = PRESETS[chip.dataset.preset];

    if (preset) {
      els.prompt.value = preset;
      els.prompt.focus();
    }
  });
});

checkHealth();