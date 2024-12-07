from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Dynamic response keywords and answers
faq_data = {
    "hi":"Hi There !",
    "ketan sup":"hi hi hi",
    "courses": "ABESIT offers undergraduate courses in B.Tech (CSE, IT, ECE, ME, CE) and MBA programs.",
    "admission": "You can apply online through our official website. Applications are open from April to July every year.",
    "hostel fees": "The hostel fees for ABESIT are ₹85,000 per year. This includes accommodation, meals, and utilities.",
    "location": "ABESIT is located in Ghaziabad, Uttar Pradesh, India.",
    "contact number": "You can contact the admissions office at +91-1234567890.",
    "semester start": "The new semester typically begins in the first week of August for all courses.",
    "library timings": "The library is open from 9:00 AM to 8:00 PM, Monday to Saturday.",
    "online materials": "You can access online study materials through the ABESIT Student Portal. Use your student ID and password to log in.",
    "sports facilities": "ABESIT offers a wide range of sports facilities, including a cricket ground, football field, basketball court, and indoor sports like table tennis and badminton.",
    "scholarships": "Yes, scholarships are available based on merit and financial need. Visit our Scholarship section on the official website for more details.",
    "fee payment": "Fees can be paid online through the ABESIT portal or directly at the accounts office on campus.",
    "events": "The upcoming events include the TechFest on January 20th and the Annual Cultural Fest on February 10th.",
    "campus visit": "Yes, campus visits are welcome. Please contact the admissions office to schedule your visit.",
    "exam schedule": "The exam schedule is published on the ABESIT portal two weeks before the exam dates.",
    "results": "Results are announced online on the ABESIT Student Portal. Use your student credentials to log in.",
    "what are placements results": "ABESIT has a strong placement cell, with top recruiters including TCS, Infosys, Wipro, and Cognizant.",
    "internships": "Internships are encouraged for all students. Opportunities are posted on the ABESIT Student Portal and through the placement cell.",
    "clubs": "ABESIT has various student clubs such as Robotics Club, Coding Club, Drama Club, and Sports Club. Visit the Clubs section on our website for more information.",
    "canteen": "The canteen offers a variety of food options at affordable prices and is open from 8:00 AM to 7:00 PM.",
    "transport": "ABESIT provides bus services for students and staff. Contact the transport office for routes and timings.",
    "what are the courses available":"ABESIT offers undergraduate courses in B.Tech (CSE, IT, ECE, ME, CE) and MBA programs.",
}

# Dynamic responses
def get_dynamic_response(query):
    query_lower = query.lower()
    for keyword, response in faq_data.items():
        if keyword in query_lower:
            return response
    if "current date" in query_lower or "today's date" in query_lower:
        return f"Today's date is {datetime.now().strftime('%d-%m-%Y')}."
    if "time" in query_lower:
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    return "I'm sorry, I don't have an answer to that question. Please contact our support team."

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_query = request.json.get("query", "").strip()
    response = get_dynamic_response(user_query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
