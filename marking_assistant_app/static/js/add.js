// Add event listeners for dynamic task and criteria creation
document.addEventListener("DOMContentLoaded", function () {
    // Add click event listener to the "Add Task" button
    var addTaskButton = document.querySelector(".add-task");
    addTaskButton.addEventListener("click", addTask);
    // Add click event listener to dynamically created "Add Criteria" buttons
    document.addEventListener("click", function (event) {
        // Check if the clicked element has the class "add-criteria"
        if (event.target.classList.contains("add-criteria")) {
            // Call the addCriteria function when an "Add Criteria" button is clicked
            addCriteria(event.target);
        }
    });
});
function addTask() {
    var taskContainer = document.getElementById("task-container");
    var taskDiv = document.createElement("div");
    taskDiv.className = "task";
    // Define HTML structure for task
    taskDiv.innerHTML = "\n        <hr>\n        <h3>Task Details</h3>\n        <label for=\"task_number\">Task Number:</label>\n        <input type=\"text\" name=\"task_number[]\" required>\n        <label for=\"task_total_mark\">Total Mark for Task:</label>\n        <input type=\"number\" name=\"task_total_mark[]\" required>\n\n        <div class=\"criteria-container\">\n            <h4>Criteria Details</h4>\n            <div class=\"criteria\">\n                <label for=\"criteria_number\">Criteria Number:</label>\n                <input type=\"text\" name=\"criteria_number[]\" required>\n                <label for=\"description\">Description:</label>\n                <input type=\"text\" name=\"description[]\" required>\n                <label for=\"marks\">Marks:</label>\n                <input type=\"number\" name=\"marks[]\" required>\n                <label for=\"feedback_comment\">Feedback Comment:</label>\n                <input type=\"text\" name=\"feedback_comment[]\">\n            </div>\n        </div>\n        <button type=\"button\" class=\"add-criteria\">Add Criteria</button>\n    ";
    taskContainer.appendChild(taskDiv);
}
function addCriteria(button) {
    var _a;
    var criteriaContainer = (_a = button.parentElement) === null || _a === void 0 ? void 0 : _a.querySelector(".criteria-container");
    var criteriaDiv = document.createElement("div");
    criteriaDiv.className = "criteria";
    // Define HTML structure for criteria
    criteriaDiv.innerHTML = "\n        <label for=\"criteria_number\">Criteria Number:</label>\n        <input type=\"text\" name=\"criteria_number[]\" required>\n        <label for=\"description\">Description:</label>\n        <input type=\"text\" name=\"description[]\" required>\n        <label for=\"marks\">Marks:</label>\n        <input type=\"number\" name=\"marks[]\" required>\n        <label for=\"feedback_comment\">Feedback Comment:</label>\n        <input type=\"text\" name=\"feedback_comment[]\">\n    ";
    criteriaContainer.appendChild(criteriaDiv);
}
