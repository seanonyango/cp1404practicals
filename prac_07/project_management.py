import datetime
from project import Project

"""Error handling and exception handling are yet to be included. This will be uploaded in later commits
Priority was placed on app functionality assuming no input error"""

INPUT_FILE = "projects.txt"

MENU = ("\n(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n"
        "(A)dd new project\n(U)pdate project\n(Q)uit")


def main():
    """Main function to run the program."""
    projects = load_projects("projects.txt")
    print(f"Loaded {len(projects)} projects from {INPUT_FILE}")
    choice = None

    while not choice == "q":
        print(MENU)
        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            filtered_projects = filter_projects_by_date(projects, date_string)
            for project in filtered_projects:
                print(project)
        elif choice == 'a':
            add_project(projects)
        elif choice == 'u':
            update_project(projects)
        else:
            print("Invalid choice")

    if input("Would you like to save to projects.txt? (yes/no) ").lower() == 'yes':
        save_projects(INPUT_FILE, projects)
    print("Thank you for using custom-built project management software.")


def project_from_string(project_string):
    """Create a Project class from a string."""
    parts = project_string.strip().split('\t')
    return Project(parts[0], parts[1], int(parts[2]), parts[3], int(parts[4]))


def load_projects(filename):
    """Load projects from a specified file."""
    projects = []
    with open(filename, 'r') as file:
        next(file)  # Skip header
        for line in file:
            projects.append(project_from_string(line))
    return projects


def save_projects(filename, projects):
    """Save projects to a specified file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percent\n")
        for project in projects:
            file.write(project.project_to_string() + '\n')


def display_projects(projects):
    """Display incomplete and completed projects."""
    incomplete = [p for p in projects if not p.is_complete()]
    completed = [p for p in projects if p.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete, key=lambda x: x.priority):
        print(project)

    print("Completed projects:")
    for project in sorted(completed, key=lambda x: x.priority):
        print(project)


def filter_projects_by_date(projects, date_string):
    """Filter projects that start after a specified date."""
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [p for p in projects if p.start_date > filter_date]
    return sorted(filtered_projects, key=lambda x: x.start_date)


def add_project(projects):
    """Add a new project to the list."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = input("Cost estimate: $")
    completion_percent = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percent))


def update_project(projects):
    """Update an existing project's details."""
    for idx, project in enumerate(projects):
        print(f"{idx} {project}")
    choice = int(input("Project choice: "))
    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")

    if new_percentage:
        projects[choice].completion_percent = int(new_percentage)
    if new_priority:
        projects[choice].priority = int(new_priority)


if __name__ == "__main__":
    main()
