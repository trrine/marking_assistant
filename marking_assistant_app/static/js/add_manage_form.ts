// FUNCTIONALITY FOR ADDING TASK

document.addEventListener("DOMContentLoaded", () => {
    const addTaskButton = document.querySelector(".add-task") as HTMLButtonElement;
    addTaskButton.addEventListener("click", addTask);
});

function addTask() {
    const taskContainer = document.getElementById("task-container") as HTMLDivElement;
    const taskDiv = document.createElement("div");
    taskDiv.className = "task";

    taskDiv.innerHTML = `
        <h3>Task Details</h3>
        <input type="hidden" name="task_id[]" value="">
        <label for="task_number">Task Number:</label>
        <input type="number" name="task_number[]" required>
        <label for="task_total_marks">Total Mark for Task:</label>
        <input type="number" name="task_total_marks[]" required>

        <div class="criteria-container">
            <h4>Criteria Details</h4>
            <div class="criteria">
                <input type="hidden" name="criteria_id[]" value="">
                <label for="criteria_number">Criteria Number:</label>
                <input type="number" name="criteria_number[]" required>
                <label for="description">Description:</label>
                <textarea name="description[]" rows="4" cols="50" required></textarea> 
                <label for="marks">Marks:</label>
                <input type="number" name="marks[]" required>
                <label for="feedback_comment">Feedback Comment:</label>
                <textarea name="feedback_comment[]" rows="4" cols="50"></textarea> 
                <button type="button" class="delete-criteria">Delete Criteria</button> 
            </div>
        </div>
        <button type="button" class="add-criteria">Add Criteria</button>
        <button type="button" class="delete-task">Delete Task</button>
    `;

    taskContainer.appendChild(taskDiv);
}

// FUNCTIONALITY FOR ADDING CRITERIA

document.addEventListener("click", (event) => {
    // Check if the clicked element has the class "add-criteria"
    if ((event.target as HTMLElement).classList.contains("add-criteria")) {
        // Call the addCriteria function when an "Add Criteria" button is clicked
        addCriteria(event.target as HTMLButtonElement);
    }
});

function addCriteria(button: HTMLButtonElement) {
    const criteriaContainer = button.parentElement?.querySelector(".criteria-container") as HTMLDivElement;
    const criteriaDiv = document.createElement("div");
    criteriaDiv.className = "criteria";

    criteriaDiv.innerHTML = `
        <label for="criteria_number">Criteria Number:</label>
        <input type="text" name="criteria_number[]" required>
        <label for="description">Description:</label>
        <textarea name="description[]" rows="4" cols="50" required></textarea> 
        <label for="marks">Marks:</label>
        <input type="number" name="marks[]" required>
        <label for="feedback_comment">Feedback Comment:</label>
        <textarea name="feedback_comment[]" rows="4" cols="50"></textarea>
        <button type="button" class="delete-criteria">Delete Criteria</button> 
    `;

    criteriaContainer.appendChild(criteriaDiv);
}

// FUNCTIONALITY FOR DELETING TASK 

document.addEventListener("click", (event) => {
    if ((event.target as HTMLElement).classList.contains("delete-task")) {
        deleteTask(event.target as HTMLButtonElement);
    }
});

function deleteTask(button: HTMLButtonElement) {
    const taskDiv = button.parentElement as HTMLDivElement;
    const taskContainer = taskDiv.parentElement as HTMLDivElement;
    taskContainer.removeChild(taskDiv);
}

// FUNCTIONALITY FOR DELETING CRITERIA 

document.addEventListener("click", (event) => {
    if ((event.target as HTMLElement).classList.contains("delete-criteria")) {
        deleteCriteria(event.target as HTMLButtonElement);
    }
});

function deleteCriteria(button: HTMLButtonElement) {
    const criteriaDiv = button.parentElement as HTMLDivElement;
    const criteriaContainer = criteriaDiv.parentElement as HTMLDivElement;
    criteriaContainer.removeChild(criteriaDiv);
}

// FUNCTIONALITY FOR DELETING ASSIGNMENT

document.addEventListener("DOMContentLoaded", () => {
    const deleteAssignmentButton = document.querySelector(".delete-assignment") as HTMLButtonElement | null;

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