export interface SentimentResponse {
  sentiment?: string;
  error?: string;
}

/**
 * Call the FastAPI backend via Vite proxy (`/predict`).
 * Backend expects: { text: string }
 * Backend returns: { sentiment: "positive" | "negative", ... }
 */
export async function analyzeText(text: string): Promise<SentimentResponse> {
  const res = await fetch("/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text }),
  });

  if (!res.ok) {
    throw new Error("Backend request failed");
  }

  return res.json();
}

