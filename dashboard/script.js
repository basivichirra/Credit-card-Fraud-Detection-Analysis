let demoFeatures = null;

async function testTransaction() {

    const amount = parseFloat(
        document.getElementById("amount").value
    );

    const transactionTime = parseFloat(
        document.getElementById("transactionTime").value
    );

    if (isNaN(amount) || amount <= 0) {
        document.getElementById("status").textContent =
            "Please enter a valid transaction amount.";
        return;
    }

    if (isNaN(transactionTime)) {
        document.getElementById("status").textContent =
            "Please enter a valid transaction time.";
        return;
    }

    document.getElementById("status").textContent =
        "Analyzing transaction...";

    let features;

    if (demoFeatures) {

        features = [...demoFeatures];

        features[0] = transactionTime;
        features[29] = amount;

    } else {

        features = [
            transactionTime,
            -16.5265065691,
            8.5849717959,
            -18.6498531852,
            9.5055935151,
            -0.34,
            0.46,
            0.23,
            0.10,
            0.36,
            0.09,
            -0.55,
            -0.62,
            -0.99,
            -0.31,
            -0.17,
            0.21,
            0.03,
            0.02,
            0.04,
            0.01,
            -0.01,
            -0.02,
            -0.03,
            0.01,
            0.02,
            0.01,
            -0.01,
            0.02,
            amount
        ];
    }

    const transaction = {
        features: features
    };

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/predict",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(transaction)
            }
        );

        const result = await response.json();

        if (!response.ok) {
            throw new Error(
                result.error || "API request failed"
            );
        }

        document.getElementById("probability").textContent =
            (result.fraud_probability * 100).toFixed(2) + "%";

        document.getElementById("riskScore").textContent =
            result.risk_score + "/100";

        document.getElementById("riskLevel").textContent =
            result.risk_level;

        document.getElementById("decision").textContent =
            result.decision;

        const factors =
            document.getElementById("riskFactors");

        factors.innerHTML = "";

        result.risk_factors.forEach(factor => {

            const div = document.createElement("div");

            div.className = "risk-factor";

            div.textContent =
                factor.feature +
                " → " +
                factor.effect +
                " fraud risk";

            factors.appendChild(div);
        });

        document.getElementById("status").textContent =
            "Analysis completed successfully.";

        addTransactionToHistory(amount, result);

    } catch (error) {

        document.getElementById("status").textContent =
            "Unable to connect to AI Risk Manager API.";

        console.error(error);
    }
}


async function loadNormalTransaction() {

    await loadDemoTransaction("normal");
}


async function loadSuspiciousTransaction() {

    await loadDemoTransaction("suspicious");
}


async function loadFraudTransaction() {

    await loadDemoTransaction("fraud");
}


async function loadDemoTransaction(scenario) {

    document.getElementById("status").textContent =
        "Loading " + scenario + " transaction...";

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/demo/" + scenario
        );

        const result = await response.json();

        if (!response.ok) {
            throw new Error(
                result.error || "Unable to load demo transaction"
            );
        }

        demoFeatures = result.features;

        document.getElementById("amount").value =
            demoFeatures[29];

        document.getElementById("transactionTime").value =
            demoFeatures[0];

        if (scenario === "normal") {

            document.getElementById("status").textContent =
                "Real legitimate transaction loaded.";

        } else if (scenario === "suspicious") {

            document.getElementById("status").textContent =
                "Demo suspicious transaction loaded.";

        } else {

            document.getElementById("status").textContent =
                "Real fraudulent transaction loaded.";
        }

    } catch (error) {

        document.getElementById("status").textContent =
            "Unable to load demo transaction.";

        console.error(error);
    }
}


function addTransactionToHistory(amount, result) {

    const history =
        document.getElementById("transactionHistory");

    const emptyRow =
        history.querySelector("td[colspan='5']");

    if (emptyRow) {
        history.innerHTML = "";
    }

    const row = document.createElement("tr");

    const transactionId =
        "TX-" + Date.now().toString().slice(-6);

    let decisionClass = "";

    if (result.decision === "BLOCK") {

        decisionClass = "transaction-block";

    } else if (result.decision === "REVIEW") {

        decisionClass = "transaction-review";

    } else {

        decisionClass = "transaction-approve";
    }

    row.innerHTML = `
        <td>${transactionId}</td>
        <td>₹${amount.toFixed(2)}</td>
        <td>${result.risk_score}/100</td>
        <td>${result.risk_level}</td>
        <td class="${decisionClass}">
            ${result.decision}
        </td>
    `;

    history.prepend(row);
}