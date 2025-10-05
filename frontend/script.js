const input = document.getElementById("promptInput");
const responseDiv = document.getElementById("response");
const sendBtn = document.getElementById("sendBtn");
const welcomeMsg = document.querySelector(".welcome_msg");

// Para poner el foco en el input
document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("promptInput").focus();
});

// Para recargar y crear nuevo chat
document.querySelector(".bot_image").addEventListener("click", () => {
    location.reload();
});

// Función para enviar el prompt al backend
async function sendPrompt() {
    const prompt = input.value.trim();
    if (!prompt) return;
    if (welcomeMsg) welcomeMsg.style.display = "none";

    // Mostrar contenedor y desactivar controles
    responseDiv.style.display = "block";
    input.value = "";
    input.disabled = true;
    sendBtn.disabled = true;

    // Contenedor de interacción
    const exchange = document.createElement("div");
    exchange.style.marginBottom = "18px";
    exchange.style.paddingBottom = "10px";
    exchange.style.borderBottom = "1px solid #1f2937";

    // Mensaje del usuario
    const userMsg = document.createElement("div");
    userMsg.textContent = "Tú: " + prompt;
    userMsg.style.color = "#60a5fa";
    userMsg.style.marginBottom = "6px";
    exchange.appendChild(userMsg);

    // Mensaje "pensando"
    const thinkingMsg = document.createElement("div");
    thinkingMsg.textContent = "Vanessa IA: Pensando...";
    thinkingMsg.style.color = "#9ca3af";
    exchange.appendChild(thinkingMsg);

    responseDiv.appendChild(exchange);
    responseDiv.scrollTop = responseDiv.scrollHeight;

    try {
        const res = await fetch("/vanessa-ia/process-prompt", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ prompt })
        });

        if (!res.ok) throw new Error("Error en la respuesta del servidor");
        const data = await res.json();

        // Eliminar mensaje "pensando"
        thinkingMsg.remove();

        const aiMsg = document.createElement("div");
        aiMsg.style.marginBottom = "12px";

        let content = data.response;

        // Si la respuesta está vacía
        if (!content || (typeof content === "string" && content.trim() === "") ||
            (Array.isArray(content) && content.length === 0)) {
            aiMsg.textContent = "Vanessa IA: No se encontraron resultados.";
            exchange.appendChild(aiMsg);
            responseDiv.scrollTop = responseDiv.scrollHeight;
            input.disabled = false;
            sendBtn.disabled = false;
            input.focus();
            return;
        }

        // Si es texto plano
        if (typeof content === "string") {
            aiMsg.textContent = "Vanessa IA: " + content;
        }
        // Si es JSON (array de registros)
        else if (Array.isArray(content)) {
            const table = document.createElement("table");
            table.style.borderCollapse = "collapse";
            table.style.width = "100%";
            table.style.marginTop = "8px";

            // Encabezados
            const headers = Object.keys(content[0]);
            const thead = document.createElement("thead");
            const headerRow = document.createElement("tr");
            headers.forEach(h => {
                const th = document.createElement("th");
                th.textContent = h.toUpperCase();
                th.style.border = "1px solid #374151";
                th.style.padding = "6px";
                th.style.background = "#1f2937";
                th.style.color = "#93c5fd";
                headerRow.appendChild(th);
            });
            thead.appendChild(headerRow);
            table.appendChild(thead);

            // Filas
            const tbody = document.createElement("tbody");
            content.forEach(row => {
                const tr = document.createElement("tr");
                headers.forEach(h => {
                    const td = document.createElement("td");
                    td.textContent = row[h];
                    td.style.border = "1px solid #374151";
                    td.style.padding = "6px";
                    tr.appendChild(td);
                });
                tbody.appendChild(tr);
            });
            table.appendChild(tbody);

            aiMsg.innerHTML = "<strong>Vanessa IA:</strong>";
            aiMsg.appendChild(table);
        } else {
            aiMsg.textContent = "Vanessa IA: Sin respuesta válida.";
        }

        exchange.appendChild(aiMsg);

    } catch (err) {
        thinkingMsg.remove();
        const aiMsg = document.createElement("div");
        aiMsg.textContent = "Vanessa IA: Ocurrió un error al obtener la respuesta, inténtalo nuevamente.";
        exchange.appendChild(aiMsg);
        console.error(err);
    }

    // Reactivar controles y hacer scroll al final
    responseDiv.scrollTop = responseDiv.scrollHeight;
    input.disabled = false;
    sendBtn.disabled = false;
    input.focus();
}

// Eventos para enviar el prompt
sendBtn.addEventListener("click", sendPrompt);
input.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        sendPrompt();
    }
});
