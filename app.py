import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Load the grades
grades = np.load("./data/grades.npy", allow_pickle=True).item()

# Split the grades into separate lists
physics_grades = grades["physics"]
computer_science_grades = grades["computer science"]
english_grades = grades["english"]
art_grades = grades["art"]
law_grades = grades["law"]
engineering_grades = grades["engineering"]
chemistry_grades = grades["chemistry"]

# streamlit setup
st.set_page_config(
    page_title="Student Report Card Prototype", page_icon="📚", layout="wide"
)

st.title("Student Report Card Prototype")

# Student Grade Selector:
with st.sidebar:
    st.title("Grade Selector")
    st.write("Input Grades of Demo Student to see changes in the report card")

    physics_grade = st.slider(
        "Physics Grade", min_value=40, max_value=100, step=1, value=physics_grades[0]
    )
    computer_science_grade = st.slider(
        "Computer Science Grade",
        min_value=40,
        max_value=100,
        step=1,
        value=computer_science_grades[0],
    )
    english_grade = st.slider(
        "English Grade", min_value=40, max_value=100, step=1, value=english_grades[0]
    )
    art_grade = st.slider(
        "Art Grade", min_value=40, max_value=100, step=1, value=art_grades[0]
    )
    law_grade = st.slider(
        "Law Grade", min_value=40, max_value=100, step=1, value=law_grades[0]
    )
    engineering_grade = st.slider(
        "Engineering Grade",
        min_value=40,
        max_value=100,
        step=1,
        value=engineering_grades[0],
    )
    chemistry_grade = st.slider(
        "Chemistry Grade",
        min_value=40,
        max_value=100,
        step=1,
        value=chemistry_grades[0],
    )

avg_physics_grade = int(np.mean(physics_grades))
avg_computer_science_grade = int(np.mean(computer_science_grades))
avg_english_grade = int(np.mean(english_grades))
avg_art_grade = int(np.mean(art_grades))
avg_law_grade = int(np.mean(law_grades))
avg_engineering_grade = int(np.mean(engineering_grades))
avg_chemistry_grade = int(np.mean(chemistry_grades))

student_grades = {
    "Physics": physics_grade,
    "Computer Science": computer_science_grade,
    "English": english_grade,
    "Art": art_grade,
    "Law": law_grade,
    "Engineering": engineering_grade,
    "Chemistry": chemistry_grade,
}

st.subheader("Grades Table")
teacher_comment = "I looked up at the mass of signs and stars in the night sky and laid myself open for the first time to the benign indifference of the world."

ovr_display_table = {
    "Subject": [
        "Physics",
        "Computer Science",
        "English",
        "Art",
        "Law",
        "Engineering",
        "Chemistry",
    ],
    "Grade": [
        physics_grade,
        computer_science_grade,
        english_grade,
        art_grade,
        law_grade,
        engineering_grade,
        chemistry_grade,
    ],
    "Average Grade": [
        avg_physics_grade,
        avg_computer_science_grade,
        avg_english_grade,
        avg_art_grade,
        avg_law_grade,
        avg_engineering_grade,
        avg_chemistry_grade,
    ],
    "Teacher Comments": [
        teacher_comment,
        teacher_comment,
        teacher_comment,
        teacher_comment,
        teacher_comment,
        teacher_comment,
        teacher_comment,
    ],
    "Absences": [0, 0, 0, 0, 0, 0, 0],
    "Late": [0, 0, 0, 0, 0, 0, 0],
}
df = pd.DataFrame(ovr_display_table)

st.dataframe(df, use_container_width=True)

st.divider()
st.subheader("Charts And Analysis")


block_1, block_2, block_3 = st.columns(3)

# create plotly radar chart for demo student, with comparison to class average:
fig = go.Figure()
fig.add_trace(
    go.Scatterpolar(
        r=[
            avg_physics_grade,
            avg_computer_science_grade,
            avg_english_grade,
            avg_art_grade,
            avg_law_grade,
            avg_engineering_grade,
            avg_chemistry_grade,
        ],
        theta=[
            "Physics",
            "Computer Science",
            "English",
            "Art",
            "Law",
            "Engineering",
            "Chemistry",
        ],
        fill="toself",
        name="Class Average",
        line=dict(color="red"),
    )
)
fig.add_trace(
    go.Scatterpolar(
        r=[
            physics_grade,
            computer_science_grade,
            english_grade,
            art_grade,
            law_grade,
            engineering_grade,
            chemistry_grade,
        ],
        theta=[
            "Physics",
            "Computer Science",
            "English",
            "Art",
            "Law",
            "Engineering",
            "Chemistry",
        ],
        fill="toself",
        name="Demo Student",
        line=dict(color="blue"),
    )
)


fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[40, 100])),
    showlegend=True,
)


block_1.plotly_chart(fig, use_container_width=True)


# now a bar graph for each subject, and a line graph for the class average (both on same chart):
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=[
            "Physics",
            "Computer Science",
            "English",
            "Art",
            "Law",
            "Engineering",
            "Chemistry",
        ],
        y=[
            physics_grade,
            computer_science_grade,
            english_grade,
            art_grade,
            law_grade,
            engineering_grade,
            chemistry_grade,
        ],
        name="Demo Student",
    )
)

fig.add_trace(
    go.Scatter(
        x=[
            "Physics",
            "Computer Science",
            "English",
            "Art",
            "Law",
            "Engineering",
            "Chemistry",
        ],
        y=[
            avg_physics_grade,
            avg_computer_science_grade,
            avg_english_grade,
            avg_art_grade,
            avg_law_grade,
            avg_engineering_grade,
            avg_chemistry_grade,
        ],
        name="Class Average",
        mode="lines+markers",
        marker_color="red",
    )
)

fig.update_layout(
    title="Demo Student Grades vs Class Average",
    xaxis_title="Subject",
    yaxis_title="Grade",
    barmode="group",
    yaxis_range=[40, 100],
)

fig.update_traces(opacity=0.7)

block_2.plotly_chart(fig, use_container_width=True)

# Now calculate the average grade for every index for each subject, and create donut chart:
# Eg. the mean of the first index of each subject, the mean of the second index of each subject, etc.
avg_grades = []
for i in range(len(physics_grades)):
    avg_grades.append(
        int(
            np.mean(
                [
                    physics_grades[i],
                    computer_science_grades[i],
                    english_grades[i],
                    art_grades[i],
                    law_grades[i],
                    engineering_grades[i],
                    chemistry_grades[i],
                ]
            )
        )
    )

# now split into categories of less than 50, 50-69, 70-79, 80-89, 90-100
less_than_50 = 0
fifty_to_69 = 0
seventy_to_79 = 0
eighty_to_89 = 0
ninety_to_100 = 0

for grade in avg_grades:
    if grade < 50:
        less_than_50 += 1
    elif grade < 70:
        fifty_to_69 += 1
    elif grade < 80:
        seventy_to_79 += 1
    elif grade < 90:
        eighty_to_89 += 1
    else:
        ninety_to_100 += 1

fig = go.Figure(
    data=[
        go.Pie(
            labels=["<50", "50-69", "70-79", "80-89", "90-100"],
            values=[
                less_than_50,
                fifty_to_69,
                seventy_to_79,
                eighty_to_89,
                ninety_to_100,
            ],
        )
    ]
)

fig.update_traces(
    hoverinfo="label+percent", textinfo="value", textfont_size=20, hole=0.3
)

fig.update_layout(title="Average Grade Distribution", showlegend=True)

block_3.plotly_chart(fig, use_container_width=True)

block_4, block_5, block_6, block_7 = st.columns([2, 1, 1, 1])

# add a histogram distribution of the average grades:
fig = go.Figure(data=[go.Histogram(x=avg_grades, nbinsx=20)])

fig.update_layout(
    title="Average Grade Distribution", xaxis_title="Grade", yaxis_title="Frequency"
)
fig.update_traces(marker_line_color="white", marker_line_width=0.5, opacity=0.7)

demo_student_avg = int(
    np.mean(
        [
            physics_grade,
            computer_science_grade,
            english_grade,
            art_grade,
            law_grade,
            engineering_grade,
            chemistry_grade,
        ]
    )
)

fig.add_vline(
    x=demo_student_avg,
    line_dash="dash",
    line_color="black",
    annotation_text=f"Demo Student Avg: {demo_student_avg}",
    annotation_position="top",
)

block_4.plotly_chart(fig, use_container_width=True)


with block_5:
    for _ in range(5):
        st.markdown("#")
    st.metric(label="Demo Student Average Grade", value=f"{demo_student_avg} %")


with block_6:
    for _ in range(5):
        st.markdown("#")
    st.metric(label="Class Average Grade", value=f"{int(np.mean(avg_grades))} %")

with block_7:
    for _ in range(5):
        st.markdown("#")
    st.metric(
        label="Percentile",
        value=f"{int(sum(np.abs(avg_grades) < demo_student_avg) / float(len(avg_grades))*100)}th",
    )

st.divider()

st.subheader("Individual Subject Analysis")

subject = st.selectbox(
    "Select Subject",
    [
        "Physics",
        "Computer Science",
        "English",
        "Art",
        "Law",
        "Engineering",
        "Chemistry",
    ],
)


st.markdown("#")

grade = student_grades[subject]

avg_grade = int(np.mean(grades[subject.lower()]))

block_8, block_9, block_10, block_11 = st.columns(4)

with block_8:
    st.metric(label="Demo Student Grade", value=f"{grade} %")

with block_9:
    st.metric(label="Class Average Grade", value=f"{avg_grade} %")

with block_10:
    st.metric(
        label="Percentile",
        value=f"{int(sum(np.abs(grades[subject.lower()]) < grade) / float(len(grades[subject.lower()]))*100)}th",
    )

with block_11:
    st.markdown(f"**Teacher Comments**: {teacher_comment}")

block_12, block_13 = st.columns(2)


# create histogram of grades for selected subject and mark a line where the demo student's grade is
fig = go.Figure(data=[go.Histogram(x=grades[subject.lower()], nbinsx=20)])

fig.update_layout(
    title=f"{subject} Grade Distribution", xaxis_title="Grade", yaxis_title="Frequency"
)
fig.update_traces(marker_line_color="white", marker_line_width=0.5, opacity=0.7)

fig.add_vline(
    x=grade,
    line_dash="dash",
    line_color="black",
    annotation_text=f"Demo Student Grade: {grade}",
    annotation_position="top",
)

block_12.plotly_chart(fig, use_container_width=True)

# create donut chart for grade distribution of selected subject
less_than_50 = 0
fifty_to_69 = 0
seventy_to_79 = 0
eighty_to_89 = 0
ninety_to_100 = 0

for grade in grades[subject.lower()]:
    if grade < 50:
        less_than_50 += 1
    elif grade < 70:
        fifty_to_69 += 1
    elif grade < 80:
        seventy_to_79 += 1
    elif grade < 90:
        eighty_to_89 += 1
    else:
        ninety_to_100 += 1

fig = go.Figure(
    data=[
        go.Pie(
            labels=["<50", "50-69", "70-79", "80-89", "90-100"],
            values=[
                less_than_50,
                fifty_to_69,
                seventy_to_79,
                eighty_to_89,
                ninety_to_100,
            ],
        )
    ]
)

fig.update_traces(
    hoverinfo="label+percent", textinfo="value", textfont_size=20, hole=0.3
)

fig.update_layout(title=f"{subject} Grade Distribution", showlegend=True)

block_13.plotly_chart(fig, use_container_width=True)
