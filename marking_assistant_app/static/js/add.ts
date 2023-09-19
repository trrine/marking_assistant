// Add event listeners for dynamic task and criteria creation
document.addEventListener("DOMContentLoaded", () => {
    // Add click event listener to the "Add Task" button
    const addTaskButton = document.querySelector(".add-task") as HTMLButtonElement;
    addTaskButton.addEventListener("click", addTask);

    // Add click event listener to dynamically created "Add Criteria" buttons
    document.addEventListener("click", (event) => {
        // Check if the clicked element has the class "add-criteria"
        if ((event.target as HTMLElement).classList.contains("add-criteria")) {
            // Call the addCriteria function when an "Add Criteria" button is clicked
            addCriteria(event.target as HTMLButtonElement);
        }
    });
});

function addTask() {
    const taskContainer = document.getElementById("task-container") as HTMLDivElement;
    const taskDiv = document.createElement("div");
    taskDiv.className = "task";

    // Define HTML structure for task
    taskDiv.innerHTML = `
        <hr>
        <h3>Task Details</h3>
        <label for="task_number">Task Number:</label>
        <input type="number" name="task_number[]" required>
        <label for="task_total_marks">Total Mark for Task:</label>
        <input type="number" name="task_total_marks[]" required>

        <div class="criteria-container">
            <h4>Criteria Details</h4>
            <div class="criteria">
                <label for="criteria_number">Criteria Number:</label>
                <input type="number" name="criteria_number[]" required>
                <label for="description">Description:</label>
                <textarea name="description[]" rows="4" cols="50" required></textarea> <!-- Use textarea for description -->
                <label for="marks">Marks:</label>
                <input type="number" name="marks[]" required>
                <label for="feedback_comment">Feedback Comment:</label>
                <textarea name="feedback_comment[]" rows="4" cols="50"></textarea> <!-- Use textarea for feedback_comment -->
            </div>
        </div>
        <button type="button" class="add-criteria">Add Criteria</button>
    `;

    taskContainer.appendChild(taskDiv);
}

function addCriteria(button: HTMLButtonElement) {
    const criteriaContainer = button.parentElement?.querySelector(".criteria-container") as HTMLDivElement;
    const criteriaDiv = document.createElement("div");
    criteriaDiv.className = "criteria";

    // Define HTML structure for criteria
    criteriaDiv.innerHTML = `
        <label for="criteria_number">Criteria Number:</label>
        <input type="text" name="criteria_number[]" required>
        <label for="description">Description:</label>
        <textarea name="description[]" rows="4" cols="50" required></textarea> <!-- Use textarea for description -->
        <label for="marks">Marks:</label>
        <input type="number" name="marks[]" required>
        <label for="feedback_comment">Feedback Comment:</label>
        <textarea name="feedback_comment[]" rows="4" cols="50"></textarea> <!-- Use textarea for feedback_comment -->
    `;

    criteriaContainer.appendChild(criteriaDiv);
}