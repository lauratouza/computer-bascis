# Function to evaluate pass/fail status
def evaluate_pass_fail(exam_score, total_classes, attended_classes):
    min_score = 70
    min_attendance_percentage = 80
    
    # Calculate attendance percentage
    attendance_percentage = (attended_classes / total_classes) * 100
    
    # Determine pass/fail status
    if exam_score >= min_score and attendance_percentage >= min_attendance_percentage:
        return "Pass"
    else:
        return "Fail"

# Inputs
exam_score = float(input("Enter the exam score (out of 100): ") or "75")
total_classes = int(input("Enter the total number of classes: ") or "40")
attended_classes = int(input("Enter the number of classes attended: ") or "32")

# Evaluation
result = evaluate_pass_fail(exam_score, total_classes, attended_classes)

# Output
print(f"The student has a status of: {result}")
