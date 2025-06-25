import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import pandas as pd

# CSS personnalisé modifié avec palette unifiée
st.markdown("""
<style>
    :root {
        --primary: #667eea;
        --secondary: #764ba2;
        --accent: #4facfe;
        --light: #a3bded;
        --highlight: #f093fb;
    }
    
    .main-header {
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .phase-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 5px solid var(--primary);
        transition: transform 0.3s ease;
    }
    
    .phase-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    .timeline-item {
        background: linear-gradient(45deg, var(--light) 0%, var(--primary) 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        text-align: center;
        font-weight: bold;
    }
    
    .stat-card {
        background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        margin: 0.5rem;
    }
    
    .future-card {
        background: linear-gradient(135deg, var(--secondary) 0%, var(--highlight) 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

## Barre de navigation
# Barre principale
navbar1 = option_menu(
    menu_title=None,
    options=["Accueil", "Prediction"],
    icons=["house-fill", "shield-check"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {
            "background-color": "transparent",
            "border": "1px solid rgba(102, 126, 234, 0.2)",
            "border-radius": "15px",
            "padding": "0.5rem",
            "margin-bottom": "2rem"
        },
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "margin": "0px",
            "padding": "0.75rem 1.5rem",
            "border-radius": "10px",
            "font-weight": "600",
            "transition": "all 0.3s ease"
        },
        "nav-link-selected": {
            "background": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
            "color": "white",
            "box-shadow": "0 8px 25px rgba(102, 126, 234, 0.3)"
        },
        "nav-link:hover": {
            "background-color": "rgba(102, 126, 234, 0.1)"
        }
    }
)

# Barre secondaire
navbar2 = option_menu(
    menu_title=None,
    options=["Historique"],
    icons=["clock", "gear"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"background-color": "#f0f2f6"},
        "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px"},
        "nav-link-selected": {"background-color": "#764ba2"},
    }
)

# Navigation
if navbar1 == "Prediction":
    st.switch_page("pages/prediction.py")

if navbar2 == "Historique":
    # En-tête principal
    st.markdown("""
    <div class="main-header">
        <h1>🏦 Évolution de l'IA dans la Détection de Fraude Bancaire</h1>
        <p>Un voyage à travers les innovations technologiques qui transforment la sécurité financière</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Timeline interactive
    st.markdown("## Chronologie de l'évolution")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown("""
        <div class="timeline-item">1990s-2000s<br>Règles Statiques</div>
        <div class="timeline-item">2000s-2010s<br>Machine Learning</div>
        <div class="timeline-item">2010s-2020s<br>Deep Learning</div>
        <div class="timeline-item">2020s+<br>IA Avancée</div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Graphique d'évolution
        years = [1995, 2005, 2015, 2025]
        efficiency = [30, 60, 85, 95]
        complexity = [20, 45, 80, 95]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=years, y=efficiency, mode='lines+markers', 
                                name='Efficacité de détection (%)', 
                                line=dict(color='#667eea', width=4)))
        fig.add_trace(go.Scatter(x=years, y=complexity, mode='lines+markers', 
                                name='Complexité des menaces (%)', 
                                line=dict(color='#f093fb', width=4)))
        
        fig.update_layout(
            title="Évolution de l'efficacité vs complexité des menaces",
            xaxis_title="Années",
            yaxis_title="Pourcentage (%)",
            template="plotly_white",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

    # Phases détaillées
    st.markdown("## 🔍 Les Phases d'Évolution Détaillées")

    st.markdown("""
    <style>
    .phases-container {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        justify-content: center;
    }
    .phase-card {
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        background-color: #ffffff;
        flex: 1;
        min-width: 280px;
        max-width: 350px;
        border-left: 5px solid #667eea !important;
        transition: transform 0.3s ease;
    }
    .phase-card:hover {
        transform: translateY(-5px) !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15) !important;
    }
    .phase-card h3 {
        color: #0056b3;
        margin-top: 0;
        margin-bottom: 15px;
    }
    .phase-card p {
        margin-bottom: 8px;
        line-height: 1.5;
    }
    .phase-card strong {
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="phases-container">
        <div class="phase-card">
            <h3>Phase 1: Systèmes basés sur des règles (1990s-2000s)</h3>
            <p><strong>Caractéristiques:</strong> Systèmes statiques basés sur des règles prédéfinies (montant maximal, zone géographique)</p>
            <p><strong>Avantages:</strong> Simplicité, efficacité contre les fraudes basiques</p>
            <p><strong>Limites:</strong> Rigidité, nombreux faux positifs, inefficace contre les fraudes sophistiquées</p>
        </div>
        <div class="phase-card">
            <h3>Phase 2: Introduction de l'apprentissage automatique (2000s-2010s)</h3>
            <p><strong>Innovation:</strong> Analyse comportementale et détection de patterns dans les données</p>
            <p><strong>Avancées:</strong> Réduction des faux positifs, meilleure précision, approche adaptative</p>
            <p><strong>Impact:</strong> Transition vers une détection plus intelligente et flexible</p>
        </div>
        <div class="phase-card">
            <h3>Phase 3: IA avancée et détection en temps réel (2010s-2020s)</h3>
            <p><strong>Technologies:</strong> Deep learning, réseaux neuronaux, analyse de centaines de variables</p>
            <p><strong>Capacités:</strong> Détection en temps réel, apprentissage continu, adaptation aux nouvelles menaces</p>
            <p><strong>Résultats:</strong> Protection proactive et dynamique contre les fraudes complexes</p>
        </div>
        <div class="phase-card">
            <h3>Phase 4: Intégration technologique avancée (2020s+)</h3>
            <p><strong>Convergence:</strong> IA + Biométrie comportementale + Blockchain + IoT</p>
            <p><strong>Innovations:</strong> Prévention de l'usurpation d'identité, analyse multi-sources</p>
            <p><strong>Sécurité:</strong> Protection renforcée contre phishing et cyberattaques</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Statistiques impressionnantes
    st.markdown("## Résultats Concrets")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="stat-card">
            <h2>30%</h2>
            <p>Réduction du taux de fraude<br>Grande banque européenne</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-card">
            <h2>95%</h2>
            <p>Précision de détection<br>avec l'IA moderne</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-card">
            <h2>Real-time</h2>
            <p>Analyse instantanée<br>des transactions</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Technologies actuelles
    st.markdown("## Technologies Actuelles")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Intelligence Artificielle Avancée:**
        - Deep Learning et réseaux neuronaux
        - Apprentissage automatique adaptatif
        - Analyse comportementale en temps réel
        - Traitement de centaines de variables simultanément
        """)
        
        st.markdown("""
        **Sécurité Renforcée:**
        - Biométrie comportementale
        - Détection d'usurpation d'identité
        - Protection anti-phishing
        - Authentification multi-facteurs
        """)
    
    with col2:
        # Graphique des technologies
        tech_data = pd.DataFrame({
            'Technologie': ['Deep Learning', 'Biométrie', 'Blockchain', 'IoT', 'ML Classique'],
            'Adoption': [85, 70, 45, 35, 95],
            'Efficacité': [95, 88, 75, 60, 70]
        })
        
        fig = px.scatter(tech_data, x='Adoption', y='Efficacité', 
                        size='Efficacité', color='Technologie',
                        title="Adoption vs Efficacité des Technologies",
                        color_discrete_sequence=['#667eea', '#764ba2', '#4facfe', '#f093fb', '#a3bded'])
        fig.update_layout(
            height=400,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Perspectives futures
    st.markdown("## Perspectives d'Avenir")
    
    st.markdown("""
    <div class="future-card">
        <h3>L'Avenir de la Détection de Fraude</h3>
        <ul>
            <li><strong>Personnalisation accrue:</strong> Systèmes adaptés au comportement individuel de chaque client</li>
            <li><strong>IA explicable:</strong> Transparence dans les décisions algorithmiques</li>
            <li><strong>Prédiction proactive:</strong> Anticipation des nouvelles formes de fraude</li>
            <li><strong>Intégration totale:</strong> Écosystème unifié Blockchain + IoT + IA</li>
            <li><strong>Temps réel augmenté:</strong> Réaction instantanée aux menaces émergentes</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
