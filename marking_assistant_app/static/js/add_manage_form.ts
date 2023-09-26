// FUNCTIONALITY FOR ADDING TASK
document.addEventListener("DOMContentLoaded", () => {
    const addTaskButton = document.querySelector("[data-action='add-task']") as HTMLButtonElement;
    addTaskButton.addEventListener("click", addTask);
});

function addTask() {
    const taskContainer = document.getElementById("task-container") as HTMLDivElement;
    const taskDiv = document.createElement("div");
    taskDiv.className = "task card";
    taskDiv.innerHTML = `
        <div class="card-body">
            <h3 class="card-title">Task Details</h3>
            <input type="hidden" name="task_id[]" value="">
            <div class="mb-3">
                <label for="task_number" class="form-label">Task Number:</label>
                <input type="number" name="task_number[]" class="form-control" required>
            </div>
            <div class="mb-3">
                <label for="task_total_marks" class="form-label">Total Mark for Task:</label>
                <input type="number" name="task_total_marks[]" class="form-control" required>
            </div>
            <div class="criteria-container">
            </div>
            <button type="button" data-action="add-criteria" class="btn btn-primary add-button">Add Criteria</button>
            <button type="button" data-action="delete-task" class="btn btn-primary">Delete Task</button>
        </div>
    `;
    taskContainer.appendChild(taskDiv);
}

// FUNCTIONALITY FOR ADDING CRITERIA
document.addEventListener("click", (event) => {
    const button = event.target as HTMLElement;
    const action = button.getAttribute("data-action");

    if (action === "add-criteria") {
        const criteriaContainer = button.closest(".task")?.querySelector(".criteria-container") as HTMLDivElement;
        const taskNumberInput = criteriaContainer.parentElement?.querySelector("input[name='task_number[]']") as HTMLInputElement;
        addCriteria(button as HTMLButtonElement, criteriaContainer, taskNumberInput);
    }
});

function addCriteria(button: HTMLButtonElement, criteriaContainer: HTMLDivElement, taskNumberInput: HTMLInputElement) {
    const criteriaDiv = document.createElement("div");
    criteriaDiv.className = "criteria";
    criteriaDiv.innerHTML = `
            <h4 class="card-title">Criteria Details</h4>
            <input type="hidden" name="criteria_id[]" value="">
            <input type="hidden" name="task_for_criteria[]" value="${taskNumberInput.value}">
            <div class="mb-3">
                <label for="description" class="form-label">Description:</label>
                <textarea name="description[]" class="form-control" rows="4" cols="50" required></textarea>
            </div>
            <div class="mb-3">
                <label for="marks" class="form-label">Marks:</label>
                <input type="number" name="marks[]" class="form-control" required>
            </div>
            <div class="mb-3">
                <label for="feedback_comment" class="form-label">Feedback Comment:</label>
                <textarea name="feedback_comment[]" placeholder="Write a feedback comment for when the criteria has not been met"
                    class="form-control" rows="4" cols="50"></textarea>
            </div>
            <button type="button" data-action="delete-criteria" class="btn btn-primary">Delete Criteria</button>
            <hr/>
    `;
    criteriaContainer.appendChild(criteriaDiv);
}

// FUNCTIONALITY FOR DELETING TASK
document.addEventListener("click", (event) => {
    const button = event.target as HTMLElement;
    const action = button.getAttribute("data-action");

    if (action === "delete-task") {
        deleteTask(button as HTMLButtonElement);
    }
});

function deleteTask(button: HTMLButtonElement) {
    const taskDiv = button.closest(".task") as HTMLDivElement;
    const taskContainer = taskDiv.parentElement as HTMLDivElement;
    taskContainer.removeChild(taskDiv);
}

// FUNCTIONALITY FOR DELETING CRITERIA
document.addEventListener("click", (event) => {
    const button = event.target as HTMLElement;
    const action = button.getAttribute("data-action");

    if (action === "delete-criteria") {
        deleteCriteria(button as HTMLButtonElement);
    }
});

function deleteCriteria(button: HTMLButtonElement) {
    const criteriaDiv = button.closest(".criteria") as HTMLDivElement;
    const criteriaContainer = criteriaDiv.parentElement as HTMLDivElement;
    criteriaContainer.removeChild(criteriaDiv);
}

// FUNCTIONALITY FOR DELETING ASSIGNMENT
document.addEventListener("DOMContentLoaded", () => {
    const deleteAssignmentButton = document.querySelector("[data-action='delete-assignment']") as HTMLButtonElement | null;

    if (deleteAssignmentButton) {
        deleteAssignmentButton.addEventListener("click", deleteAssignment);
    }
});

function deleteAssignment() {
    const confirmDelete = confirm("Are you sure you want to delete this assignment?");

    if (confirmDelete) {
        const form = document.querySelector("form") as HTMLFormElement | null;

        if (form) {
            const input = document.createElement("input");
            input.type = "hidden";
            input.name = "delete_assignment";
            input.value = "1";
            form.appendChild(input);
            form.submit();
        }
    }
}
