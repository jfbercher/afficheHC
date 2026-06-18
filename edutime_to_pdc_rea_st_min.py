U='HETP'
T='%.2f'
S=round
R=KeyError
H=True
D='Total (HETD)'
C='Total (HETP)'
import streamlit as A,pandas as I
A.set_page_config(page_title='Analyse HETP / HETD',layout='wide')
A.title('📊 Analyse des heures (HETP / HETD)')
V,W=A.columns(2)
with V:X=A.number_input('Total des heures dues au statut (en HETP), sans les décharges',value=4e2,step=.5,format=T)
with W:Y=A.number_input('Total des décharges (en HETP)',value=1e2,step=.5,format=T)
J=X-Y
A.write('Total des heures attendues (en HETP) :',J)
A.markdown('---')
P=A.file_uploader('Choisissez votre fichier CSV',type=['csv'])
def Z(df_input,out_mode):B=out_mode;C=df_input.copy();A=I.pivot_table(data=C,index=['Cours'],columns=['Activité'],aggfunc=['sum'],fill_value=0,values=[B],margins=H,margins_name=f"Total ({B})");A.columns=[A[2]for A in A.columns];A.index.name='ECUE';return A
if P is not None:
	try:
		a=I.read_csv(P,sep=';',decimal=',');b,c=A.tabs([U,'HETD'])
		with b:
			A.subheader('Tableau HETP')
			try:G=Z(a,U);A.dataframe(G,use_container_width=H)
			except R:A.error("La colonne 'HETP' est introuvable dans le fichier fourni.")
		I.set_option('display.precision',2);K=G.apply(lambda x:x*2/3).rename(index={C:D},columns={C:D})
		with c:
			A.subheader('Tableau HETD')
			try:A.dataframe(K,use_container_width=H)
			except R:A.error("La colonne 'HETD' est introuvable dans le fichier fourni.")
		E=G.loc[C,C];L=K.loc[D,D];A.write('Total des heures réalisées : ',S(E,2),' HETP, soit ',S(L,2),'HETD.');B=E-J;Q=B*2/3
		if B>0:M=39.01;F=43.5;N=F/1.5;O=min(200,B)*M+max(0,B-200)*N
		E=G.loc[C,C];L=K.loc[D,D];B=E-J;Q=B*2/3;A.markdown('#### Synthèse des Heures');A.markdown('\n    <style>\n    /* Taille du titre (Label) */\n    [data-testid="stMetricLabel"] {\n        font-size: 14px !important;\n    }\n    \n    /* Taille de la valeur principale */\n    [data-testid="stMetricValue"] {\n        font-size: 24px !important; /* Par défaut ~40px */\n    }\n    \n    /* Taille du delta (sous-valeur en HETD) */\n    [data-testid="stMetricDelta"] {\n        font-size: 18px !important;\n    }\n    </style>\n    ',unsafe_allow_html=H);d,e=A.columns(2)
		with d:A.metric(label='⏳ Heures Réalisées',value=f"{E:.2f} HETP",delta=f"{L:.2f} HETD",delta_color='off')
		with e:f='normal'if B>=0 else'inverse';A.metric(label='➕ Heures Complémentaires',value=f"{B:.2f} HETP",delta=f"{Q:.2f} HETD",delta_color=f)
		if B>0:M=39.01;F=43.5;N=F/1.5;O=min(200,B)*M+max(0,B-200)*N;g=O/F;A.markdown('#### Rémunération');A.success(f"\n            **Rémunération attendue  : {O:.2f} €**, *soit l'équivalent de **{g:.2f} HETD** (sur la base de {F:.2f}€ / heure de TD universitaire).*\n            ")
	except Exception as h:A.error(f"Erreur lors de la lecture du fichier : {h}")
else:A.info('💡 Dans Edutime, choisir "Mes Services", sélectionner "Réalisé", "Cette année universitaire", cliquer sur "Appliquer les filtres", puis "Exporter". Utiliser le fichier csv résultant dans cette micro-appli.')