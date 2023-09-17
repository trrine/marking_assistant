// add event listeners for dynamic task and criteria creation
document.addEventListener("DOMContentLoaded", function() {
    // add click event listener to the "Add Task" button
    document.querySelector(".add-task").addEventListener("click", addTask);

    // add click event listener to dynamically created "Add Criteria" buttons
    document.addEventListener("click", function(event) {
        // check if the clicked element has the class "add-criteria"
        if (event.target.classList.contains("add-criteria")) {
            // call the addCriteria function when an "Add Criteria" button is clicked
            addCriteria(event.target);
        }
    });
});

function addTask() {
    const taskContainer = document.getElementById("task-container");
    const taskDiv = document.createElement("div");
    taskDiv.className = "task";

    // define HTML structure for task
    taskDiv.innerHTML = `
        <hr>
        <h3>Task Details</h3>
        <label for="task_number">Task Number:</label>
        <input type="text" name="task_number[]" required>
        <label for="task_total_mark">Total Mark for Task:</label>
        <input type="number" name="task_total_mark[]" required>

        <!-- Criteria details for this task (allow adding multiple criteria) -->
        <div class="criteria-container">
            <h4>Criteria Details</h4>
            <div class="criteria">
                <label for="criteria_number">Criteria Number:</label>
                <input type="text" name="criteria_number[]" required>
                <label for="description">Description:</label>
                <input type="text" name="description[]" required>
                <label for="marks">Marks:</label>
                <input type="number" name="marks[]" required>
                <label for="feedback_comment">Feedback Comment:</label>
                <input type="text" name="feedback_comment[]">
            </div>
        </div>
        <button type="button" class="add-criteria">Add Criteria</button>
    `;

    taskContainer.appendChild(taskDiv);
}

function addCriteria(button) {
    const criteriaContainer = button.parentElement.querySelector(".criteria-container");
    const criteriaDiv = document.createElement("div");
    criteriaDiv.className = "criteria";

    // define HTML structure for criteria
    criteriaDiv.innerHTML = `
        <label for="criteria_number">Criteria Number:</label>
        <input type="text" name="criteria_number[]" required>
        <label for="description">Description:</label>
        <input type="text" name="description[]" required>
        <label for="marks">Marks:</label>
        <input type="number" name="marks[]" required>
        <label for="feedback_comment">Feedback Comment:</label>
        <input type="text" name="feedback_comment[]">
    `;

    criteriaContainer.appendChild(criteriaDiv);
}