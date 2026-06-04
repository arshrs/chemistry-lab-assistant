const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const { spawn } = require("child_process");
const path = require("path");

const app = express();

app.use(cors());
app.use(bodyParser.json());

app.post("/ask", (req, res) => {

    const question = req.body.question;

    if (!question) {
        return res.json({ answer: "No question provided" });
    }

    const scriptPath = path.resolve(__dirname, "../ml-model/predict.py");

    const pythonProcess = spawn("py", [scriptPath, question]);

    let output = "";
    let errorOutput = "";

    pythonProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    pythonProcess.stderr.on("data", (data) => {
        errorOutput += data.toString();
    });

    pythonProcess.on("close", () => {

        if (errorOutput) {
            console.error("Python Error:", errorOutput);
            return res.json({ answer: "Error running model" });
        }

        try {
            const parsed = JSON.parse(output);
            res.json(parsed);   // ✅ send real JSON
        } catch (err) {
            console.error("JSON Parse Error:", err);
            res.json({ answer: output.trim() });
        }

    });

});

app.listen(5000, () => {
    console.log("Backend running on port 5000");
});