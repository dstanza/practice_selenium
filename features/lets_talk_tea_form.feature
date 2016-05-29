# Created by dstanza at 5/29/2016
Feature: Check the contact form filter
  # Enter feature description here

  Scenario: Complete form and submit
    Given I open Let's Talk Tea page
    Then I complete the form
    And I submit

#  Scenario: Leave name blank and submit
#    Given I open Let's Talk Tea page
#    Then I leave name blank
#    And I submit

#  Scenario: Add more than 255 char on name and submit
#    Given I open Let's Talk Tea page
#    Then I enter 256 character on name
#    And I submit
#
#  Scenario: Add number or symbol on name and submit
#    Given I open Let's Talk Tea page
#    Then I add number or symbol on name
#    And I submit
#
#  Scenario: Leave email blank and submit
#    Given I open Let's Talk Tea page
#    Then I leave email blank
#    And I submit
#
#  Scenario: Fill incorrect email format and submit
#    Given I open Let's Talk Tea page
#    Then I fill incorrect email format
#    And I submit