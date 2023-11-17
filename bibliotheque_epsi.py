import tkinter as tk
from tkinter import messagebox   #Importe la classe messagebox du module tkinter pour afficher des boîtes de dialogue.
import sqlite3   #Importe le module sqlite3 pour interagir avec une base de données SQLite.

class GestionLivresApp:   #Définit une classe GestionLivresApp pour encapsuler l'application.
    def ajouter_livre(self):   # Définit une méthode ajouter_livre pour ajouter un livre à la base de données.
        # Obtient les valeurs saisies dans les champs d'entrée pour le titre, l'auteur et le genre.
        titre = self.entry_titre.get()
        auteur = self.entry_auteur.get()
        genre = self.entry_genre.get()

        if titre:
            self.c.execute("INSERT INTO livres (titre, auteur, genre) VALUES (?, ?, ?)", (titre, auteur, genre))
            #INSERT INTO livres: Indique que l'on souhaite insérer des données dans la table "livres".
            #Les symboles de point d'interrogation "?" sont des espaces réservés qui seront remplacés par les 
            # valeurs réelles lors de l'exécution de la requête.
            self.conn.commit()
            #Valide la transaction en commitant les changements dans la base de données.
            messagebox.showinfo("Succès", f"Livre '{titre}' ajouté avec succès!")
        else:
            messagebox.showwarning("Erreur", "Veuillez saisir le titre du livre.")

    def supprimer_livre(self):
        titre = self.entry_titre.get() # on a besoin juste de le nom du livre

        if titre:
            self.c.execute("DELETE FROM livres WHERE titre=?", (titre,))
            # supprime toutes les lignes de la table "livres" où la valeur dans la colonne "titre" est égale à la valeur 
            # de la variable titre 
            self.conn.commit()
            messagebox.showinfo("Succès", f"Livre '{titre}' supprimé avec succès!")
        else:
            messagebox.showwarning("Erreur", "Veuillez saisir le titre du livre à supprimer.")

    def rechercher_livre(self):
        titre = self.entry_titre.get()

        if titre:
            self.c.execute("SELECT * FROM livres WHERE titre=?", (titre,))
            livre = self.c.fetchone()
            #obtenir la première ligne résultante 

            if livre:
                messagebox.showinfo("Résultat de la Recherche", f"Titre: {livre[1]}\nAuteur: {livre[2]}\nGenre: {livre[3]}")
            else:
                messagebox.showinfo("Résultat de la Recherche", "Aucun livre trouvé avec ce titre.")
        else:
            messagebox.showwarning("Erreur", "Veuillez saisir le titre du livre à rechercher.")

    def afficher_tous_les_livres(self):
        self.c.execute("SELECT * FROM livres")
        tous_les_livres = self.c.fetchall()

        if tous_les_livres:
            message = ""
            for livre in tous_les_livres:
                message += f"Titre: {livre[1]}\nAuteur: {livre[2]}\nGenre: {livre[3]}\n\n"
            messagebox.showinfo("Tous les Livres", message)
        else:
            messagebox.showinfo("Aucun Livre", "Aucun livre n'a été ajouté.")

if __name__ == "__main__":   # Vérifie si le script est exécuté en tant que programme principal.

    fenetre = tk.Tk()
    gestion_bib = GestionLivresApp()

    # Connexion à la base de données SQLite
    gestion_bib.conn = sqlite3.connect("bibliotheque.db")
    gestion_bib.c = gestion_bib.conn.cursor()

    # Interface graphique
    gestion_bib.label_titre = tk.Label(fenetre, text="Titre:")
    gestion_bib.label_titre.grid(row=0, column=0, pady=5)

    gestion_bib.entry_titre = tk.Entry(fenetre)
    gestion_bib.entry_titre.grid(row=0, column=1, pady=5)

    gestion_bib.label_auteur = tk.Label(fenetre, text="Auteur:")
    gestion_bib.label_auteur.grid(row=1, column=0, pady=5)

    gestion_bib.entry_auteur = tk.Entry(fenetre)
    gestion_bib.entry_auteur.grid(row=1, column=1, pady=5)

    gestion_bib.label_genre = tk.Label(fenetre, text="Genre:")
    gestion_bib.label_genre.grid(row=2, column=0, pady=5)

    gestion_bib.entry_genre = tk.Entry(fenetre)
    gestion_bib.entry_genre.grid(row=2, column=1, pady=5)

    gestion_bib.btn_ajouter_livre = tk.Button(fenetre, text="Ajouter Livre", command=gestion_bib.ajouter_livre)
    gestion_bib.btn_ajouter_livre.grid(columnspan=2, pady=5)

    gestion_bib.btn_supprimer_livre = tk.Button(fenetre, text="Supprimer Livre", command=gestion_bib.supprimer_livre)
    gestion_bib.btn_supprimer_livre.grid(columnspan=2, pady=5)

    gestion_bib.btn_rechercher_livre = tk.Button(fenetre, text="Rechercher Livre", command=gestion_bib.rechercher_livre)
    gestion_bib.btn_rechercher_livre.grid(columnspan=2, pady=5)

    gestion_bib.btn_afficher_tous = tk.Button(fenetre, text="Afficher Tous les Livres", command=gestion_bib.afficher_tous_les_livres)
    gestion_bib.btn_afficher_tous.grid(columnspan=2, pady=5)

    fenetre.mainloop()