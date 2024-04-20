import plotly.graph_objects as go

def plot_grades(physics_grade, computer_science_grade, english_grade, art_grade, law_grade, engineering_grade, chemistry_grade, 
                avg_physics_grade, avg_computer_science_grade, avg_english_grade, avg_art_grade, avg_law_grade, avg_engineering_grade, avg_chemistry_grade, block_1):
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
            r=[physics_grade, computer_science_grade, english_grade, art_grade, law_grade, engineering_grade, chemistry_grade],
            theta=['Physics', 'Computer Science', 'English', 'Art', 'Law', 'Engineering', 'Chemistry'],
            fill='toself',
            name='Demo Student',
            line=dict(color='blue')
        ))

    fig.add_trace(go.Scatterpolar(
            r=[avg_physics_grade, avg_computer_science_grade, avg_english_grade, avg_art_grade, avg_law_grade, avg_engineering_grade, avg_chemistry_grade],
            theta=['Physics', 'Computer Science', 'English', 'Art', 'Law', 'Engineering', 'Chemistry'],
            fill='toself',
            name='Class Average',
            line=dict(color='red')
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[40, 100]
            )),
        showlegend=True
    )

    block_1.plotly_chart(fig)