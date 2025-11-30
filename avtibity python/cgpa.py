
def marks_to_grade_point(marks):
    if marks >= 90:
        return 10  # O
    elif marks >= 80:
        return 9   # A+
    elif marks >= 70:
        return 8   # A
    elif marks >= 60:
        return 7   # B+
    elif marks >= 50:
        return 6   # B
    elif marks >= 40:
        return 5   # C
    elif marks >= 30:
        return 4   # D
    else:
        return 0   # E, F, G, I


def calculate_tgpa(credits, marks):
    total_weighted_points = 0
    total_credits = 0
    
    for i in range(len(credits)):
        grade_point = marks_to_grade_point(marks[i])
        total_weighted_points += grade_point * credits[i]
        total_credits += credits[i]
    

    tgpa = total_weighted_points / total_credits if total_credits > 0 else 0
    return tgpa


def calculate_cgpa(terms_credits, terms_marks):
    total_weighted_points = 0
    total_credits = 0
    
    for i in range(len(terms_credits)):
        tgpa = calculate_tgpa(terms_credits[i], terms_marks[i])
        total_weighted_points += tgpa * sum(terms_credits[i])  
        total_credits += sum(terms_credits[i])  
    
    
    cgpa = total_weighted_points / total_credits if total_credits > 0 else 0
    return cgpa


def main():
    
    num_terms = int(input("Enter the number of terms: "))
    

    all_terms_credits = []
    all_terms_marks = []
    

    for t in range(1, num_terms + 1):
        print(f"\nFor Term {t}:")
        num_subjects = int(input("Enter the number of subjects: "))
        
        credits = []
        marks = []
        
        for s in range(1, num_subjects + 1):
            credit = int(input(f"Enter credits for subject {s}: "))
            mark = int(input(f"Enter marks for subject {s} (out of 100): "))
            
            credits.append(credit)
            marks.append(mark)
        
        all_terms_credits.append(credits)
        all_terms_marks.append(marks)
    

    for t in range(1, num_terms + 1):
        tgpa = calculate_tgpa(all_terms_credits[t-1], all_terms_marks[t-1])
        print(f"TGPA for Term {t}: {tgpa:.2f}")
    
 
    cgpa = calculate_cgpa(all_terms_credits, all_terms_marks)
    print(f"\nYour CGPA is: {cgpa:.2f}")


if __name__ == "__main__":
    main()
