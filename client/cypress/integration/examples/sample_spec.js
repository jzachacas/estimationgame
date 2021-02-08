describe('Test login', () => {
  it('logout + login should never fail', () => {

    cy.request('/logout')
    cy.visit('/')

    cy.get('input').type('I am a bot')
    cy.get('button').click()
  })
})

describe('Test login 2', () => {
  it('Repeat for a second user', () => {

    cy.request(`/logout`)
    cy.visit(`/`)
    cy.get('input').type('I am a second bot')
    cy.get('button').click()
  })
})

describe('Change current Story', () => {
  it('Editing the description', () => {
    cy.request(`/logout`)
    cy.request(`/logout`)
    cy.visit(`/`)
    cy.get('input').type('I am a second bot')
    cy.get('button').click()

    cy.get('#edit-story-btn').click()
    cy.get('#form-title-edit-input').type('{selectall}Me demand new feature')
    cy.get('#edit-submit').click()

    cy.get('h5.card-title').should('have.text', 'Me demand new feature')
  })
})
