# Created by dstanza at 5/29/2016
Feature: Check all links
    Scenario: Open website
      Given I open PracticeSelenium website
      Then I print the title
      And print the name

    Scenario: print current url
      Given I open PracticeSelenium website
      Then I print current url

    Scenario: Browser back, forward and refresh
      Given I open PracticeSelenium website

      And I click Our Passion link
      Then I click back on the browser
      And I click forward on the browser
      And I click refresh on the browser

      And I click Menu link
      Then I click back on the browser
      And I click forward on the browser
      And I click refresh on the browser

      And I click Let's Talk Tea link
      Then I click back on the browser
      And I click forward on the browser
      And I click refresh on the browser

      And I click Check Out link
      Then I click back on the browser
      And I click forward on the browser
      And I click refresh on the browser

