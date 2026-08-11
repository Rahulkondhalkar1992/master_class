# Azure Learnings Academy
## Azure Data Engineering Master Class

Premium Streamlit course discovery + learning portal (Phase 1).

### Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

### Deploy to Streamlit Community Cloud

1. Push this repository to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io).
3. Select the repo, set main file to `app.py`.
4. Deploy.

### Folder structure

```text
azure-data-engineering-master-class/
├── app.py
├── requirements.txt
├── README.md
├── .streamlit/config.toml
├── assets/
├── content/          # Structured course content
├── components/       # UI building blocks + CSS
├── views/            # Page renderers (custom sidebar routing)
└── utils/            # Navigation, WhatsApp, validators
```

> `views/` is used instead of Streamlit's auto `pages/` folder so the premium custom sidebar remains the single navigation system.

### WhatsApp contacts

- https://wa.me/918655448143
- https://wa.me/918692016111

### Phase 1 scope

Included: Home, Course Info, Roadmap, Syllabus, Why Program, Live Classes, Project, Interviews, Assignments, Tools, Support, SQL/Python practice UI previews, AI Assistant (coming soon), Enquiry form.

Not included yet: login, databases, practice execution engines, AI chat backend, payments, certificates.
