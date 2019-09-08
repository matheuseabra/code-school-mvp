import React, { Component } from 'react';

import api from '../services/api';

import Card from '../components/Card';

class SignUp extends Component {
  constructor() {
    super();
    this.state = {
        username: '',
        email: '',
        loading: false
    };

    this.handleOnChange = this.handleOnChange.bind(this);
    this.handleLogin = this.handleLogin.bind(this);
  }


  handleOnChange = e => this.setState({ [e.target.name]: e.target.value });

  async handleLogin(e) {
    e.preventDefault();
    this.setState({ loading: true });
    await api.post('/users', this.state);
    console.log(this.state);
  }

  render() {
    const { username, email } = this.state;
    return (
      <div className="mdl-grid">
        <div className="mdl-cell">
          <Card>
            <div className="mdl-card__title mdl-card--expand">
              <h2 className="mdl-card__title-text font-sc">Sign Up</h2>
            </div>
            <div className="mdl-card__supporting-text">
              <div className="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
                <input
                  onChange={this.handleOnChange}
                  className="mdl-textfield__input"
                  type="text"
                  value={username}
                  name="username"
                />
                <label className="mdl-textfield__label" htmlFor="username">
                  Username
                </label>
              </div>
              <div className="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
                <input
                  onChange={this.handleOnChange}
                  className="mdl-textfield__input"
                  type="email"
                  value={email}
                  name="email"
                />
                <label className="mdl-textfield__label" htmlFor="email">
                  Email
                </label>
              </div>
            </div>
            <div className="mdl-card__actions mdl-card--border ">
              <button
                type="submit"
                onSubmit={this.handleLogin}
                className="mdl-button font-sc mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent"
              >
                Register
              </button>
            </div>
          </Card>
        </div>
      </div>
    );
  }
}

export default SignUp;