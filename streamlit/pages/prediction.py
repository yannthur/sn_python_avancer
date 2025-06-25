import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from pycaret.classification import load_model, predict_model

# Configuration de la page
st.set_page_config(
    page_title="Détection de Fraude",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personnalisé pour améliorer le design
st.markdown("""
<style>
    /* Styles généraux */
    .main {
        padding-top: 2rem;
    }
    
    /* Titre principal */
    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 2rem;
        text-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Conteneur du formulaire */
    .form-container {
        background: linear-gradient(145deg, #ffffff 0%, #f8f9ff 100%);
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.1);
        border: 1px solid rgba(102, 126, 234, 0.1);
        margin: 2rem 0;
    }
    
    /* Titre du formulaire */
    .form-title {
        text-align: center;
        color: #4a5568;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 2rem;
        position: relative;
    }
    
    .form-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 80px;
        height: 3px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 2px;
    }
    
    /* Cartes de résultat */
    .prediction-card {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 15px 35px rgba(79, 172, 254, 0.3);
        animation: slideInUp 0.6s ease-out;
    }
    
    .fraud-card {
        background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 15px 35px rgba(255, 65, 108, 0.3);
        animation: slideInUp 0.6s ease-out;
        border: 2px solid rgba(255, 255, 255, 0.2);
    }
    
    .prediction-card h2, .fraud-card h2 {
        margin: 0 0 1rem 0;
        font-size: 1.8rem;
        font-weight: 700;
    }
    
    .prediction-card p, .fraud-card p {
        margin: 0.5rem 0;
        font-size: 1.1rem;
        opacity: 0.95;
    }
    
    /* Légende */
    .prediction-legend {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-top: 2rem;
        padding: 1.5rem;
        background: rgba(255, 255, 255, 0.8);
        border-radius: 12px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .legend-item {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        font-weight: 600;
        color: #4a5568;
    }
    
    .color-box {
        width: 20px;
        height: 20px;
        border-radius: 6px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* Animations */
    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Amélioration des inputs Streamlit */
    .stSlider > div > div > div > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    }
    
    .stNumberInput > div > div > input {
        border-radius: 8px;
        border: 2px solid #e2e8f0;
        transition: all 0.3s ease;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    .stSelectbox > div > div > div {
        border-radius: 8px;
        border: 2px solid #e2e8f0;
    }
    
    /* Bouton de soumission */
    .stFormSubmitButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3) !important;
    }
    
    .stFormSubmitButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 35px rgba(102, 126, 234, 0.4) !important;
    }
    
    /* Radio buttons */
    .stRadio > div {
        background: rgba(255, 255, 255, 0.5);
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid rgba(102, 126, 234, 0.1);
    }
    
    /* Colonnes */
    .stColumn {
        padding: 0 1rem;
    }
    
    /* Espacement */
    .element-container {
        margin-bottom: 1.5rem;
    }
    
    /* Style pour les labels */
    .stSlider label, .stNumberInput label, .stSelectbox label, .stRadio label {
        font-weight: 600 !important;
        color: #4a5568 !important;
        font-size: 1rem !important;
    }
</style>
""", unsafe_allow_html=True)

# Navbar avec design amélioré
navbar1 = option_menu(
    menu_title=None,
    options=["Accueil", "Prediction"],
    icons=["house-fill", "shield-check"],
    menu_icon="cast",
    default_index=1,
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

# Titre principal avec style amélioré
st.markdown('<h1 class="main-title">🛡️ Détection de Fraude Bancaire</h1>', unsafe_allow_html=True)

if navbar1 == "Accueil":
    st.switch_page("pages/acceuil.py")


# Formulaire de saisie avec design amélioré
with st.form("prediction_form"):
    st.markdown('<h3 class="form-title">🔍 Analysez une transaction bancaire</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("### 👤 Informations personnelles")
        age = st.slider("Âge du titulaire du compte", 18, 100, 30, help="Âge du titulaire du compte bancaire")
        salaire = st.number_input("Salaire annuel ($)", min_value=0, max_value=1000000, value=50000, step=1000, help="Revenu annuel brut")
        credit_score = st.slider("Score de crédit", 300, 850, 700, help="Score de crédit FICO (300-850)")
        montant_transaction = st.number_input("Montant de la transaction ($)", min_value=0.0, value=500.0, step=50.0, help="Montant de la transaction à analyser")
    
    with col2:
        st.markdown("### 🏛️ Détails du compte")
        anciennete = st.slider("Ancienneté du compte (années)", 0, 50, 5, help="Nombre d'années depuis l'ouverture du compte")
        carte_type = st.selectbox("Type de carte", ["Visa", "Mastercard"], index=0, help="Type de carte bancaire utilisée")
        region = st.selectbox("Région", ["Houston", "Orlando", "Miami"], index=0, help="Région géographique de la transaction")
        genre = st.radio("Genre", ["Homme", "Femme"], horizontal=True, help="Genre du titulaire du compte")

    # Bouton de soumission avec espacement
    st.markdown("<br>", unsafe_allow_html=True)
    soumettre = st.form_submit_button("🔍 Analyser la transaction", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# Conversion des données en format numérique
carte_type_mapping = {"Visa": 0, "Mastercard": 1}
region_mapping = {"Houston": 0, "Orlando": 1, "Miami": 2}
genre_mapping = {"Homme": 1, "Femme": 0}

if soumettre:
    with st.spinner('🔄 Analyse en cours...'):
        # Créer le DataFrame avec les données saisies
        data = pd.DataFrame({
            'age': [age],
            'salaire': [salaire],
            'score_credit': [credit_score],
            'montant_transaction': [montant_transaction],
            'anciennete_compte': [anciennete],
            'type_carte': [carte_type_mapping[carte_type]],
            'region': [region_mapping[region]],
            'genre': [genre_mapping[genre]]
        })
        
        # Charger le modèle
        try:
            model = load_model('pages/model')
            
            # Faire la prédiction
            prediction = predict_model(model, data=data)
            prediction_label = prediction['prediction_label'][0]
            prediction_score = prediction['prediction_score'][0]
            
            # Afficher le résultat avec animations
            st.markdown("---")
            
            if prediction_label == 1:  # Fraude
                st.markdown(f"""
                <div class="fraud-card">
                    <h2>TRANSACTION FRAUDULEUSE DÉTECTÉE</h2>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="prediction-card">
                    <h2>TRANSACTION LÉGITIME</h2>
                </div>
                """, unsafe_allow_html=True)
            
            # Légende explicative améliorée
            st.markdown("""
            <div class="prediction-legend">
                <div class="legend-item">
                    <div class="color-box" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);"></div>
                    <span>Transaction normale</span>
                </div>
                <div class="legend-item">
                    <div class="color-box" style="background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 100%);"></div>
                    <span>Transaction frauduleuse</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            

        except Exception as e:
            st.error(f"❌ Erreur lors de l'analyse : {str(e)}")
            st.info("💡 Vérifiez que le modèle est correctement chargé et que tous les paramètres sont valides.")