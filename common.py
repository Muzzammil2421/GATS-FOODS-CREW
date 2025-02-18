from crewai_tools import SerperDevTool, EXASearchTool

serper_search_tool = SerperDevTool()
exa_search_tool = EXASearchTool()

data_analyst_agent_role = (
        "Research and Analysis: Conduct thorough research in the following beverage categories: "
        "Functional Beverages, Carbonated Drinks, Alcoholic Beverages (e.g., wine, beer, cocktails, hard seltzer), "
        "Non-Alcoholic Drinks (e.g., mocktails, 0% alcohol beer, 0% alcohol wine), Juice Category, Soft Drinks, "
        "Flavored Water and Enhanced Water, Functional Water, Sports Drinks, Energy Drinks.\n"
        "Identify global innovations across product development, packaging, unique ingredients, health benefits, "
        "marketing campaigns, startup-driven innovations, and innovative technologies.\n"
        "Trend Summarization: Summarize findings according to specific topics. Organize information in a manner suitable "
        "for creating posts or blogs, ensuring it is well-structured and easy to transfer to a copywriter.\n"
        "Innovation Reporting: Provide regular, structured reports categorizing innovations by product, benefit, packaging, "
        "marketing, or other key aspects."
    )

data_analyst_agent_goal = "To identify and analyze reliable sources of information to uncover innovations in the beverage industry, with a focus on disruptive innovation."

data_analyst_agent_backstory = (
        "Strong analytical skills with the ability to extract meaningful insights from data. "
        "In-depth knowledge of the beverage industry and market trends. "
        "Excellent communication skills for summarizing and presenting findings. "
        "Familiarity with innovation-driven startups and emerging technologies. "
        "Proficiency in data visualization tools is a plus."
    )

content_specialist_agent_role = (
        "Transform innovative discoveries in the beverage industry into engaging and impactful content that elevates the "
        "company's voice and strengthens its market presence. Craft compelling posts and articles based on research provided "
        "by the Data Analyst, aligning with the company's tone, style, and strategic goals."
    )

content_specialist_agent_goal = (
        "Develop LinkedIn posts for each innovation provided by the Data Analyst. "
        "Ensure posts are written in a tone that is light yet professional, captivating, and concise to encourage engagement and drive readership."
    )

content_specialist_agent_backstory=(
        "Exceptionally talented Copywriter who thrives in a creative yet professional environment and aligns seamlessly with "
        "the company's innovative DNA. Skilled at crafting engaging, short-form content that captures attention while conveying expertise. "
        "Collaborate effectively with the Data Analyst and other team members. "
        "Possesses a deep understanding of B2B marketing, with a strong emphasis on the food and beverage industry."
    )

market_research_task_description = (
        "Identify and analyze reliable sources of information to uncover innovations in the beverage industry, focusing on, "
        "but not limited to, disruptive advancements in the following areas:\n\n"
        "1. Product development (e.g., new formulas, flavors, or functionalities)\n"
        "2. Packaging advancements (e.g., sustainability, convenience)\n"
        "3. Unique ingredients (e.g., plant-based compounds, functional additives)\n"
        "4. Health benefits or claims\n"
        "5. Marketing campaigns (e.g., disruptive approaches, creative strategies)\n"
        "6. Startup-driven innovations and emerging technologies."
        "You should give quantitavie insights and numbers to support interesting insights"""
    )

market_research_task_expected_output = (
        "- Organize findings into clear, categorized topics, ensuring accessibility and relevance for further processing by the Copywriter.\n"
        "- Summarize information with precision to align with content creation needs for posts and blogs.\n"
        "- Develop concise and structured summaries of trends and innovations, categorized by product type, benefits, or other key elements."
    )

content_creation_task_description = (
        "Craft engaging, impactful, and professionally aligned content that transforms research-based insights into compelling narratives for the company's social media platforms:\n\n"
        "1. Develop LinkedIn posts for each innovation identified by the Data Analyst.\n"
        "2. Ensure posts are written in a tone that is light yet professional, capturing the audience's attention and encouraging engagement.\n"
        "3. Use storytelling techniques to make technical and market insights more engaging and relatable to the audience.\n"
        "4. Ensure content remains interesting and concise while delivering value and expertise."
    )

content_creation_task_expected_output = (
        "A complete content package including:\n"
        "250-300 tokens LinkedIn posts for each innovation identified by the Data Analyst"
    )
