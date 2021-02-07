describe('Test login', () => {
  it('logout + login should never fail', () => {

    cy.request('/logout')
    cy.visit('/')

    cy.get('input').type('I am a bot')
    cy.get('button').click()
  })
})

describe('Test login', () => {
  it('logout + login should never fail', () => {

    cy.request('/logout')
    cy.visit('/')

    cy.get('input').type('I am a second bot')
    cy.get('button').click()
  })
})
