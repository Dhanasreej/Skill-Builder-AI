 **1. SkillBuilder AI**
    SkillBuilder AI is a web-based application designed to help learners generate personalized learning paths based on their current skills and future goals. The app offers structured roadmaps tailored for beginners and enhances learning through curated YouTube tutorials. Users can also download their personalized plans for offline access.

**2. Key Features**
   1. Accepts a user’s current skill and future goal.
   2. Uses Groq’s LLaMA 3 model to generate beginner-friendly, stepwise learning plans.
   3. Fetches relevant YouTube videos dynamically based on the user’s learning journey.
   4. Offers downloadable learning paths in .txt format.
   5. User-friendly interface built using Streamlit.

**3. Setup & Installation**
   ### Create the virtual environment
   python -m venv venv
   ### Activate the virtual environment on Windows:
   venv\Scripts\activate  Example: (venv) PS D:\Downloads\skillbuilder>
   ### Install dependencies
   pip install -r requirements.txt
   ### Add API keys in a .env file
   GROQ_API_KEY=groq_api_key
   YOUTUBE_API_KEY=youtube_api_key
   ### Code in app.py
   (code)
   ### Run the application using
   streamlit run app.py

**4. Usage Guide**
   1. Launch the app using the command above.
   2. Enter your current skill (e.g., Python, Cooking).
   3. Enter your desired goal (e.g., Become a Data Analyst, Become a Chef).
   4. Click the “Get Learning Path” button.
   5. The app generates:
      -A structured, beginner-friendly learning roadmap.
      -Top 5 curated YouTube tutorials related to your goal.
   6. Download your learning path using the download button for offline use.
   
**6. Architecture Overview**
    User Input -> Streamlit UI -> Groq API (LLaMA 3) -> YouTubeSearchPython -> Output Display + Download Option
   
**7. Tech Stack**
   1. Frontend: Streamlit
   2. Backend/LLM: Groq’s LLaMA 3 (via Groq API)
   3. Video Search: YouTube Search Python library
   4. Environment Management: Python virtual environment + dotenv
      
      
   
   
   




   
   


   
   


   
   

