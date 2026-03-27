export interface SentimentResponse {
  sentiment?: string;
  error?: string;
}

export async function analyzeText(text: string): Promise<SentimentResponse> {
  const res = await fetch(
    "https://sentiment-analysis-project-gazk.onrender.com/predict",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text }),
    },
  );

  if (!res.ok) {
    throw new Error("Backend request failed");
  }

  return res.json();
}
