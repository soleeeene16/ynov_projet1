/// <reference types="cypress" />


describe('My First Test', () => {
  it('visits some pages', () => {
    cy.visit('http://localhost:8501') 
  })

  it ("saisir la surface de la maison", () => {
    cy.get('input').eq(0).clear().type("1.{enter}") 
  })

  it ("saisir le nb de chambre", () => {
    cy.get('input').eq(1).clear().type("1.{enter}") 
  })

  it ("saisir si jardin", () => {
    cy.get('input').eq(2).clear().type("0.{enter}")
  })

  it ("Vérification du prix de la maison", () => {
  cy.get('p').then((valeur) => {

    console.log(valeur)
    "console.log( 'PRIX : ', valeur[0].innerText.substr(27))"

    var prixmaison= parseFloat(valeur[0].innerText.substr(27))
    cy.log("Prix max limite",prixmaison < 1000000)
    cy.log("Prix min limite",prixmaison > 20000)
    expect(prixmaison).to.be.greaterThan(20000)
    expect(prixmaison).to.be.lessThan(1000000)
    })
  })
})
