import sys
import os

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
except Exception as e:
    print(f"Import error details: {e}")
    sys.exit(1)

def build_pdf(filename="CV_Shehan_Hirusha.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    story = []
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor('#0F172A'),
        alignment=TA_CENTER
    )
    
    subtitle_style = ParagraphStyle(
        'SubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#0284C7'),
        alignment=TA_CENTER
    )
    
    contact_style = ParagraphStyle(
        'ContactInfo',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#475569'),
        alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=4
    )
    
    body_style = ParagraphStyle(
        'BodyText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#334155')
    )

    body_bold = ParagraphStyle(
        'BodyBold',
        parent=body_style,
        fontName='Helvetica-Bold'
    )
    
    # Header
    story.append(Paragraph("SHEHAN HIRUSHA", title_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("ANDROID APPLICATION DEVELOPER & SYSTEM ANALYST", subtitle_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("Vavuniya, Sri Lanka | +94 77 123 4567 | shehan.hirusha@vau.ac.lk | github.com/shehanhirusha | linkedin.com/in/shehan-hirusha-33bb52411", contact_style))
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0284C7'), spaceAfter=10))
    
    # Professional Summary
    story.append(Paragraph("PROFESSIONAL SUMMARY", heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#CBD5E1'), spaceAfter=6))
    summary_text = (
        "Passionate and detail-oriented Android Application Developer and Undergraduate ICT Student at the Faculty of "
        "Technological Studies, University of Vavuniya. Specialized in Android SDK development (Kotlin, Java, Jetpack Compose), "
        "mobile architecture (MVVM, Room, Retrofit, Firebase), and System Analysis and Design (SAD). Proven track record of "
        "designing intuitive mobile interfaces and applying UML modeling techniques to build robust Android solutions. "
        "Seeking an Android Developer or Mobile Engineering Internship."
    )
    story.append(Paragraph(summary_text, body_style))
    story.append(Spacer(1, 10))
    
    # Education
    story.append(Paragraph("EDUCATION", heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#CBD5E1'), spaceAfter=6))
    
    edu_data = [
        [
            Paragraph("<b>BSc (Hons) in Information & Communication Technology</b><br/>Faculty of Technological Studies, University of Vavuniya", body_style),
            Paragraph("<b>2023 – Present</b><br/>Vavuniya, Sri Lanka", ParagraphStyle('RightText', parent=body_style, alignment=TA_RIGHT))
        ]
    ]
    t_edu = Table(edu_data, colWidths=[380, 160])
    t_edu.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_edu)
    story.append(Spacer(1, 4))
    story.append(Paragraph("• <b>Relevant Coursework:</b> Mobile Application Development (Android), System Analysis & Design (SAD), Data Structures & Algorithms, Database Management Systems, Object-Oriented Software Engineering.", body_style))
    story.append(Paragraph("• <b>Academic Distinction:</b> Dean's List for Academic Excellence (Semester 1 & 2). GPA: 3.82 / 4.00.", body_style))
    story.append(Spacer(1, 10))
    
    # Technical Skills
    story.append(Paragraph("TECHNICAL & SOFT SKILLS", heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#CBD5E1'), spaceAfter=6))
    
    skills_data = [
        [Paragraph("<b>Android & Mobile:</b>", body_style), Paragraph("Kotlin, Java, Android SDK, Jetpack Compose, XML Layouts, Material Design 3", body_style)],
        [Paragraph("<b>Mobile Architecture:</b>", body_style), Paragraph("MVVM, Coroutines, LiveData/StateFlow, Retrofit, Room DB, Firebase, REST APIs", body_style)],
        [Paragraph("<b>SAD & Modeling:</b>", body_style), Paragraph("UML (Use-Case, Activity, Sequence, ERD), Wireframing, System Requirements (FR/NFR)", body_style)],
        [Paragraph("<b>Web & Developer Tools:</b>", body_style), Paragraph("JavaScript, HTML5/CSS3, Git, GitHub, Android Studio, Postman, Figma", body_style)],
        [Paragraph("<b>Soft Skills:</b>", body_style), Paragraph("Problem Solving, Mobile UI/UX Principles, Technical Writing, Team Collaboration", body_style)]
    ]
    t_skills = Table(skills_data, colWidths=[140, 400])
    t_skills.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_skills)
    story.append(Spacer(1, 10))
    
    # Projects
    story.append(Paragraph("KEY PROJECTS", heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#CBD5E1'), spaceAfter=6))
    
    p1 = "<b>AgriConnect – Smart Agriculture Mobile App & Platform</b> | <i>Kotlin, Android SDK, Retrofit, Node.js, MySQL</i>"
    story.append(Paragraph(p1, body_bold))
    story.append(Paragraph("• <b>Problem:</b> Local farmers faced market price exploitation and distribution delays due to lack of real-time mobile market access.", body_style))
    story.append(Paragraph("• <b>Role & SAD Modeling:</b> Android Lead & System Analyst. Engineered native Android client with MVVM architecture, Room offline caching, and REST API integration.", body_style))
    story.append(Paragraph("• <b>Impact:</b> Streamlined direct farmer-to-buyer crop listing with push notifications and live pricing charts.", body_style))
    story.append(Spacer(1, 6))

    p2 = "<b>VavuCampus – University Student Resource Mobile App</b> | <i>Android SDK, Kotlin, Jetpack Compose, Firebase</i>"
    story.append(Paragraph(p2, body_bold))
    story.append(Paragraph("• <b>Problem:</b> Disorganized distribution of lecture notes and timetable conflict handling across ICT department streams.", body_style))
    story.append(Paragraph("• <b>Role:</b> Android Developer. Built responsive Material 3 mobile UI, automated schedule conflict detector, and note downloading module.", body_style))
    story.append(Paragraph("• <b>Impact:</b> Adopted by 250+ ICT undergraduates for instant mobile timetable alerts and resource downloads.", body_style))
    story.append(Spacer(1, 6))

    p3 = "<b>Medity – Tele-Health Doctor Booking Android App</b> | <i>Kotlin, Material Design 3, Coroutines, LocalStorage</i>"
    story.append(Paragraph(p3, body_bold))
    story.append(Paragraph("• <b>Problem:</b> Long queue times for outpatient consultations in regional healthcare units.", body_style))
    story.append(Paragraph("• <b>Role:</b> Mobile UI/UX Developer. Conducted requirements specification (FR/NFR) and developed interactive appointment booking Android flow.", body_style))
    story.append(Paragraph("• <b>Impact:</b> Reduced patient booking latency with automated calendar slot picking and instant confirmation alerts.", body_style))
    story.append(Spacer(1, 10))

    # Experience & Leadership
    story.append(Paragraph("LEADERSHIP & EXTRACURRICULAR ACTIVITIES", heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#CBD5E1'), spaceAfter=6))
    
    exp_data = [
        [
            Paragraph("<b>Executive Committee Member</b> | ICT Student Circle, University of Vavuniya", body_style),
            Paragraph("<b>2024 – Present</b>", ParagraphStyle('RightText2', parent=body_style, alignment=TA_RIGHT))
        ]
    ]
    t_exp = Table(exp_data, colWidths=[380, 160])
    t_exp.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_exp)
    story.append(Paragraph("• Conducted Android app development workshops covering Kotlin basics, Activity lifecycle, and Jetpack Compose for peer students.", body_style))
    story.append(Paragraph("• Co-organized annual departmental Tech Hackathon, managing workshop scheduling and technical support for 120+ participants.", body_style))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("<b>Participant & Finalist</b> | National Mobile App Hackathon 2024", body_bold))
    story.append(Paragraph("• Engineered a functional Android mobile prototype within 24 hours under the Smart Cities track.", body_style))
    story.append(Spacer(1, 10))
    
    # Certifications & Declarations
    story.append(Paragraph("CERTIFICATIONS & DECLARATIONS", heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#CBD5E1'), spaceAfter=6))
    story.append(Paragraph("• <b>Android Development Specialization:</b> Associate Android Developer Course (Google / Coursera).", body_style))
    story.append(Paragraph("• <b>System Analysis Certification:</b> Agile Software Development & Requirements Engineering (LinkedIn Learning).", body_style))
    story.append(Paragraph("• <b>Declaration:</b> I hereby certify that the information provided in this CV is accurate and authentic.", body_style))

    doc.build(story)
    print(f"Successfully generated {filename}")

if __name__ == "__main__":
    build_pdf()
