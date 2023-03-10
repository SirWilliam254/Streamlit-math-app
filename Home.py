import streamlit as st

st.set_page_config(
    page_title="Math-AI-App",
    page_icon="📈",
)

st.title("Math AI")
st.sidebar.success("Successfully Loaded")

st.write(
    """
    `Mathematics` is a very interesting faculty which has a tremendous effect on the productivity and value creation in 
this mandane world that we live in.
    In this app we have calculators for automating some of the mathematical challenges, You can explore the calculators
    on the sidebar.
    """
)

st.write(
    """
      Introducing the latest innovation in the world of mathematics - a groundbreaking app that harnesses the power of artificial intelligence to simplify complex calculations and reduce workloads for technical professionals.

Our math AI app is designed to streamline the work of engineers, scientists, and researchers who rely on complex mathematical equations and models to solve real-world problems. With our app, users can spend less time on tedious calculations and more time on critical thinking and problem-solving. Having advanced algorithms it can perform a wide range of mathematical functions, including but not limited to solving differential equations, optimizing complex systems, and performing statistical analysis. Users can input their equations and data, and our app will instantly provide accurate solutions and visualizations.

One of the most exciting features of our math AI app is its ability to learn and adapt to user preferences. As users input more data and equations, the app's algorithms become more accurate and efficient, allowing users to solve increasingly complex problems with ease.

Our app also provides users with an intuitive and user-friendly interface that makes it easy to input data and equations, visualize results, and collaborate with team members. With our app, users can work more efficiently and effectively, leading to better results and faster innovation.
   """
)



# Footer
c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Twitter: [@william-mburu](https://twitter.com/WilliamCinemat)**', icon="👋")
with c2:
    st.info('**GitHub: [@SirWilliam254](https://github.com/Sirwilliam254)**', icon="💻")
with c3:
    st.info('**LinkedIn: [William Mburu](https://www.linkedin.com/in/william-mburu/)**', icon="🌍")
