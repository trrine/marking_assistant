// FUNCTIONALITY FOR ADDING TASK
document.addEventListener("DOMContentLoaded", function () {
    var addTaskButton = document.querySelector("[data-action='add-task']");
    addTaskButton.addEventListener("click", addTask);
});
function addTask() {
    var taskContainer = document.getElementById("task-container");
    var taskDiv = document.createElement("div");
    taskDiv.className = "task card";
    taskDiv.innerHTML = "\n        <div class=\"card-body\">\n            <h3 class=\"card-title\">Task Details</h3>\n            <input type=\"hidden\" name=\"task_id[]\" value=\"\">\n            <div class=\"mb-3\">\n                <label for=\"task_number\" class=\"form-label\">Task Number:</label>\n                <input type=\"number\" name=\"task_number[]\" class=\"form-control\" required>\n            </div>\n            <div class=\"mb-3\">\n                <label for=\"task_total_marks\" class=\"form-label\">Total Mark for Task:</label>\n                <input type=\"number\" step=\"0.01\" name=\"task_total_marks[]\" class=\"form-control\" required>\n            </div>\n            <div class=\"criteria-container\">\n            </div>\n            <div class=\"button-container\">\n                <button type=\"button\" data-action=\"add-criteria\" class=\"btn btn-secondary add-button\">Add Criteria</button>\n                <button type=\"button\" data-action=\"delete-task\" class=\"btn btn-primary\">Delete Task</button>\n            </div>\n        </div>\n    ";
    taskContainer.appendChild(taskDiv);
}
// FUNCTIONALITY FOR ADDING CRITERIA
document.addEventListener("click", function (event) {
    var _a, _b;
    var button = event.target;
    var action = button.getAttribute("data-action");
    if (action === "add-criteria") {
        var criteriaContainer = (_a = button.closest(".task")) === null || _a === void 0 ? void 0 : _a.querySelector(".criteria-container");
        var taskNumberInput = (_b = criteriaContainer.parentElement) === null || _b === void 0 ? void 0 : _b.querySelector("input[name='task_number[]']");
        addCriteria(button, criteriaContainer, taskNumberInput);
    }
});
function addCriteria(button, criteriaContainer, taskNumberInput) {
    var criteriaDiv = document.createElement("div");
    criteriaDiv.className = "criteria";
    criteriaDiv.innerHTML = "\n            <h4 class=\"card-title\">Criteria Details</h4>\n            <input type=\"hidden\" name=\"criteria_id[]\" value=\"\">\n            <input type=\"hidden\" name=\"task_for_criteria[]\" value=\"".concat(taskNumberInput.value, "\">\n            <div class=\"mb-3\">\n                <label for=\"description\" class=\"form-label\">Description:</label>\n                <textarea name=\"description[]\" class=\"form-control\" rows=\"4\" cols=\"50\" required></textarea>\n            </div>\n            <div class=\"mb-3\">\n                <label for=\"marks\" class=\"form-label\">Marks:</label>\n                <input type=\"number\" step=\"0.01\" name=\"marks[]\" class=\"form-control\" required>\n            </div>\n            <div class=\"mb-3\">\n                <label for=\"feedback_comment\" class=\"form-label\">Feedback Comment:</label>\n                <textarea name=\"feedback_comment[]\" placeholder=\"Write a feedback comment for when the criteria has not been met\"\n                    class=\"form-control\" rows=\"4\" cols=\"50\"></textarea>\n            </div>\n            <div class=\"button-container\">\n                <button type=\"button\" data-action=\"delete-criteria\" class=\"btn btn-primary\">Delete Criteria</button>\n            </div>\n            <hr/>\n    ");
    criteriaContainer.appendChild(criteriaDiv);
}
// FUNCTIONALITY FOR DELETING TASK
document.addEventListener("click", function (event) {
    var button = event.target;
    var action = button.getAttribute("data-action");
    if (action === "delete-task") {
        deleteTask(button);
    }
});
function deleteTask(button) {
    var taskDiv = button.closest(".task");
    var taskContainer = taskDiv.parentElement;
    taskContainer.removeChild(taskDiv);
}
// FUNCTIONALITY FOR DELETING CRITERIA
document.addEventListener("click", function (event) {
    var button = event.target;
    var action = button.getAttribute("data-action");
    if (action === "delete-criteria") {
        deleteCriteria(button);
    }
});
function deleteCriteria(button) {
    var criteriaDiv = button.closest(".criteria");
    var criteriaContainer = criteriaDiv.parentElement;
    criteriaContainer.removeChild(criteriaDiv);
}
// FUNCTIONALITY FOR DELETING ASSIGNMENT
document.addEventListener("DOMContentLoaded", function () {
    var deleteAssignmentButton = document.querySelector("[data-action='delete-assignment']");
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
