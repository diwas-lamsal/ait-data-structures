################################################################
################################################################
# Deleting bozo user
################################################################
################################################################

Given("I am an an admin") do
  @user = FactoryBot.create :admin

  # Also creating teacher only to populate the list of users
  @teacher = FactoryBot.create :teacher
end

Given("there is a bozo user I want to delete") do
  @student = FactoryBot.create :student_user
end

When("I visit the Admin Dashboard") do
  visit("/site/admin_dashboard")
end

Then("I should see a list of users") do
  expect(page).to have_content(@user.email)
  expect(page).to have_content(@teacher.email)
  expect(page).to have_content(@student.email)
end

Then("I should see the bozo user") do
  expect(page).to have_content(@student.email)
end

When("I click delete button next to the bozo user") do
  page.find(:css, 'a[href="/site/destroy_normal/' + @student.id.to_s + '"]').click
end

Then("The bozo user should be deleted") do
  expect(page).to have_no_content(@student.email)
end

################################################################
################################################################
# Editing user
################################################################
################################################################

Given("there is a user I want to edit") do
  @user_to_edit = FactoryBot.create :student_user
end

Then("I should see the user I want to edit") do
  expect(page).to have_no_content(@student.email)
end

When("I click edit button next to the user") do
  page.find(:css, 'a[href="/site/destroy_normal/' + @student.id.to_s + '"]').click
end

Then("I should see a form to edit the user") do
  expect(page).to have_selector("#editform")
end

When("I change the details of the user") do
  pending # Write code here that turns the phrase above into concrete actions
end

Then("I should see the updated details") do
  pending # Write code here that turns the phrase above into concrete actions
end

################################################################
################################################################
