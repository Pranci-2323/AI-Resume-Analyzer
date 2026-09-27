function analyzeResume() {

    const resume = document.getElementById("resume");
    const jobDescription =
        document.getElementById("job-description").value;

    const result = document.getElementById("result");

    if (resume.files.length === 0) {
        result.innerHTML = `
            <h2>Please upload your resume ⚠️</h2>
        `;
        return;
    }

    if (jobDescription.trim() === "") {
        result.innerHTML = `
            <h2>Please enter a job description ⚠️</h2>
        `;
        return;
    }

    result.innerHTML = `
        <h2>Resume Received ✅</h2>

        <p>
            Your resume is ready for analysis.
        </p>

        <p>
            AI analysis will be added in the next step.
        </p>
    `;
}