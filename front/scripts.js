console.log("Script carregado com sucesso!");


document.addEventListener("DOMContentLoaded", function () {
  const button = document.querySelector('button[type="button"]');
  const formSection = document.getElementById("form");
  const descriptionSection = document.getElementById("app-description");

  button.addEventListener("click", function () {
    // mostra o formulário
    formSection.style.display = "block";

    // esconde a descrição
    descriptionSection.style.display = "none";
  });
});

// endpoint da API
const API_URL = 'http://127.0.0.1:5000';

// captura o formulário
const form = document.querySelector("#wellness-form");

// função para converter o formulário em JSON
function formToJSON(formElement) {
  const formData = new FormData(formElement);
  const data = {};

  for (const [key, value] of formData.entries()) {
    data[key] = value;
  }

  return data;
}

// função que chama a API
async function sendPrediction(data) {
  try {
    const response = await fetch(`${API_URL}/individuos`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    });

    if (!response.ok) {
      throw new Error(`Erro na API: ${response.status}`);
    }

    return await response.json();

  } catch (error) {
    console.error("Erro ao consumir API:", error);
    throw error;
  }
}

// handler do submit
form.addEventListener("submit", async (event) => {
  console.log("Enviando dados...");
  event.preventDefault();

  const data = formToJSON(form);

  console.log("Dados enviados:", data);

  try {
    const result = await sendPrediction(data);

    console.log("Resposta da API:", result);

    document.querySelector("#resultado").innerText =
      `Burnout Risk: ${result.prediction}`;

  } catch (error) {
    document.querySelector("#resultado").innerText =
      "Erro ao processar a requisição.";
  }
});