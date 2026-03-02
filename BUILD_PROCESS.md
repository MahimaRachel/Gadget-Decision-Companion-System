Build Process
============

How it started
====================

Goal: build a gadget comparison tool where the user defines what matters most.

Initial idea: Streamlit + pandas DataFrame with fixed ratings.

Evolution of thinking
===========================
simple table + sliders → too manual  
              │
              ▼
added SQLite → easier to manage many models  
              │
              ▼
custom model input → session state dict  

              │
              ▼
 weighted scoring + ranking table  

              │
              ▼
removal bug → tried direct session_state write → failed → callback + dynamic key  

              │
              ▼
category switch bug → added last_domain check & reset  

              │
              ▼
UI polish (card, issues section) + documentation

Alternatives considered
==========================

- Other options of Streamlit
- More advanced decision methods 
- Adding images of the gadgets→ decided against (maintenance, load time)

Refactoring decisions
====================

- Moved ratings into SQLite → easier to expand
- Used controlled list (`compared_models`) instead of relying on widget state
- Added factory function for remove callbacks → fixed stale closure problem
- Dynamic multiselect key → solved category change refresh issue

Mistakes & corrections
=========================

Mistake: tried `st.session_state[widget_key] = ...` after widget created  
→ StreamlitAPIException  
Correction: controlled list + dynamic key + rerun

Mistake: direct comparison `st.session_state.last_domain` without existence check  
→ AttributeError  
Correction: `'last_domain' not in st.session_state` guard

What changed & why
====================

- Removed images → faster prototype, less maintenance
- Changed from checkbox list to multiselect + remove buttons → better UX
- Added issues/fixes section → adds real value beyond pure scoring
