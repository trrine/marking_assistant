// FUNCTIONALITY FOR ADDING TASK
document.addEventListener("DOMContentLoaded", function () {
    var addTaskButton = document.querySelector(".add-task");
    addTaskButton.addEventListener("click", addTask);
});
function addTask() {
    var taskContainer = document.getElementById("task-container");
    var taskDiv = document.createElement("div");
    taskDiv.className = "task";
    taskDiv.innerHTML = "\n        <h3>Task Details</h3>\n        <input type=\"hidden\" name=\"task_id[]\" value=\"\">\n        <label for=\"task_number\">Task Number:</label>\n        <input type=\"number\" name=\"task_number[]\" required>\n        <label for=\"task_total_marks\">Total Mark for Task:</label>\n        <input type=\"number\" name=\"task_total_marks[]\" required>\n\n        <div class=\"criteria-container\">\n            <h4>Criteria Details</h4>\n            <div class=\"criteria\">\n                <input type=\"hidden\" name=\"criteria_id[]\" value=\"\">\n                <label for=\"criteria_number\">Criteria Number:</label>\n                <input type=\"number\" name=\"criteria_number[]\" required>\n                <label for=\"description\">Description:</label>\n                <textarea name=\"description[]\" rows=\"4\" cols=\"50\" required></textarea> \n                <label for=\"marks\">Marks:</label>\n                <input type=\"number\" name=\"marks[]\" required>\n                <label for=\"feedback_comment\">Feedback Comment:</label>\n                <textarea name=\"feedback_comment[]\" rows=\"4\" cols=\"50\"></textarea> \n                <button type=\"button\" class=\"delete-criteria\">Delete Criteria</button> \n            </div>\n        </div>\n        <button type=\"button\" class=\"add-criteria\">Add Criteria</button>\n        <button type=\"button\" class=\"delete-task\">Delete Task</button>\n    ";
    taskContainer.appendChild(taskDiv);
}
// FUNCTIONALITY FOR ADDING CRITERIA
document.addEventListener("click", function (event) {
    // Check if the clicked element has the class "add-criteria"
    if (event.target.classList.contains("add-criteria")) {
        // Call the addCriteria function when an "Add Criteria" button is clicked
        addCriteria(event.target);
    }
});
function addCriteria(button) {
    var _a;
    var criteriaContainer = (_a = button.parentElement) === null || _a === void 0 ? void 0 : _a.querySelector(".criteria-container");
    var criteriaDiv = document.createElement("div");
    criteriaDiv.className = "criteria";
    criteriaDiv.innerHTML = "\n        <label for=\"criteria_number\">Criteria Number:</label>\n        <input type=\"text\" name=\"criteria_number[]\" required>\n        <label for=\"description\">Description:</label>\n        <textarea name=\"description[]\" rows=\"4\" cols=\"50\" required></textarea> \n        <label for=\"marks\">Marks:</label>\n        <input type=\"number\" name=\"marks[]\" required>\n        <label for=\"feedback_comment\">Feedback Comment:</label>\n        <textarea name=\"feedback_comment[]\" rows=\"4\" cols=\"50\"></textarea>\n        <button type=\"button\" class=\"delete-criteria\">Delete Criteria</button> \n    ";
    criteriaContainer.appendChild(criteriaDiv);
}
// FUNCTIONALITY FOR DELETING TASK 
document.addEventListener("click", function (event) {
    if (event.target.classList.contains("delete-task")) {
        deleteTask(event.target);
    }
});
function deleteTask(button) {
    var taskDiv = button.parentElement;
    var taskContainer = taskDiv.parentElement;
    taskContainer.removeChild(taskDiv);
}
// FUNCTIONALITY FOR DELETING CRITERIA 
document.addEventListener("click", function (event) {
    if (event.target.classList.contains("delete-criteria")) {
        deleteCriteria(event.target);
    }
});
function deleteCriteria(button) {
    var criteriaDiv = button.parentElement;
    var criteriaContainer = criteriaDiv.parentElement;
    criteriaContainer.removeChild(criteriaDiv);
}
// FUNCTIONALITY FOR DELETING ASSIGNMENT
document.addEventListener("DOMContentLoaded", function () {
    var deleteAssignmentButton = document.querySelector(".delete-assignment");
    if (deleteAssignmentButton) {
        deleteAssignmentButton.addEventListener("click", deleteAssignment);
    }
});
function deleteAssignment() {
    var confirmDelete = confirm("Are you sure you want to delete this assignment?");
    if (confirmDelete) {
        var form = document.querySelector("form");
        if (form) {
            var input = document.createElement("input");
            input.type = "hidden";
            input.name = "delete_assignment";
            input.value = "1";
            form.appendChild(input);
            form.submit();
        }
    }
}
