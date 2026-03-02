Gadget Decision Companion
========================

A personalized gadget comparison tool that ranks devices (laptops, smartphones, earbuds, tablets, smartwatches, speakers, cameras) according to user-defined priorities instead of generic reviews.

Understanding of the problem
============================

The problem is to help the user make better decisions showing the reasons.

Here the problem statement is been applied only to the decision of choosing digital gadgets.

Users are overwhelmed by too many gadget options, conflicting reviews, and sponsored content.  
Most comparison tools use fixed weights or editorial opinion.  
Goal is to let the user decide what matters most (e.g. battery > camera > price) and get an objective, transparent, weighted ranking.

Assumptions
===========
- The user's need is to find out better gadget based on his/her preferences
- Users understand 1–10 rating scale for the user's custom model of a gadget
- 1–10 ratings are linear and additive (simple weighted sum model)
- Database ratings are reasonably accurate / up-to-date (2025/2026 perspective)
- Custom models should fall back to neutral 5 if user doesn't rate every parameter
- No need for user accounts / persistence across sessions

Why this structure / design decisions
=======================================

- Streamlit : fastest way to build interactive data apps with Python-only
- SQLite : zero-setup, local, good enough for ~100–200 products
- Weighted sum scoring : simple, interpretable, fast; avoids black-box ML
- Session state for selections : avoids database writes for temporary user choices
- Dynamic multiselect key : workaround for Streamlit limitation when changing categories
- Callback + factory for remove buttons : solves loop variable capture problem

Trade-offs
==========

- Simplicity vs sophistication: weighted sum instead of more advanced MCDA methods
- No images of any gadgets: faster load, less maintenance (can be added later)
- Local database : no live web scraping / API updates
- No authentication : single-user app

Edge cases considered
=======================

- Switching category : must clear old selections (implemented with last_domain check)
- Removing items from multiselect : widget refresh workaround
- Adding custom model with same name is prevented
- No models selected : disable button to compare
- All weights = 0 : error message
- Custom model with all sliders at 5 : button disabled
- Domain with no products : warning shown

How to run the project
=========================

Install dependencies:

    pip install streamlit pandas

Run the Streamlit:
    
    streamlit run Gadget_decision_companion.py

What I would improve with more time
====================================

- Real product images (Unsplash / official APIs / local assets)
- Live price fetching (Amazon / local retailers API)
- More advanced scoring (e.g. ELECTRE, PROMETHEE, or even simple ML ranking)
- Export result as PDF / shareable link
- Dark mode / better mobile layout
- Option to save/load user preference profiles
