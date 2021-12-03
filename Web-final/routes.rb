# frozen_string_literal: true

Rails.application.routes.draw do
  get "site/get_users"
  get "site/destroy_normal/:id", to: "site#destroy_normal"
  get "site/destroy_ajax/:id", to: "site#destroy_ajax"

  get "site/edit_normal/:id", to: "site#edit_normal"
  post "site/edit_normal", to: "site#edit_normal_post"

  devise_for :users
  get "site/index"
  get "site/admin_dashboard", as: :admin_dashboard
  resources :projects
  resources :students

  post "projects/:id/students", as: :add_student_to_project, controller: :projects, action: :add_student
  root to: "site#index"
end
