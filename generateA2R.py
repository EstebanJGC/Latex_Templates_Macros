"""# ----------------------------------------------------------- #
#
# Project     : Templates
# Filename    : generateA2R.py
# Root        : ./scripts
# Author      : Dr. Esteban J. Garzón C. (esteban.garzon@unical.it)
# Created     : 08/04/2023, 22:10
#
#
# ----------------------------------------------------------- #"""


def generate_reviewer_block(reviewer_number, num_concerns):
    block = f"%============= Reviewer#{reviewer_number} ==================\n"
    block += "\\reviewersection\n"
    block += "Here Reviewer general comment (if given)\n\n"
    block += "\\replySingle{\n"
    block += "We thank the Reviewer for the time spent in reviewing our work and for its general appreciation...\n"
    block += "}\n\n"

    for concern_number in range(1, num_concerns + 1):
        block += f"% === Concern {concern_number}\n"
        block += "\\begin{point}\n"
        block += "     Here Reviewer concern...\n"
        block += "\\end{point}\n\n"
        block += "\\replyFull{\n"
        block += "We thank the Reviewer for this comment...\n"
        block += "}{\n"
        block += "\\begin{itemize}\n"
        block += "    \item \\secref{sec:Sec2}, Par. 1: \\Paste{SecIPar1}\n"
        block += "\\end{itemize}\n"
        block += "}\n\n"

    return block


# Inputs:
r = 3  # Number of reviewers
concerns = [1, 1, 2]  # Number of concerns for each reviewer
filename = "A2R.tex"

# Define the number of reviewers and their respective concerns with a Dictionary
reviewers_concerns = {i+1: c for i, c in enumerate(concerns)}

'''
# Define the number of reviewers and their respective concerns
reviewers_concerns = {
    1: 3,  # Reviewer 1 has 1 concern
    2: 1,  # Reviewer 2 has 2 concerns
    3: 1   # Reviewer 3 has 2 concerns
}'''

# Generate reviewer blocks for each reviewer with their specific number of concerns
for reviewer, num_concerns in reviewers_concerns.items():
    reviewer_block = generate_reviewer_block(reviewer, num_concerns)
    print(reviewer_block)
    print()


# Save the output to a file
'''
with open(filename, "w") as file:
    file.write(reviewer_block)
'''
