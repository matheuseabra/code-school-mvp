import React, { Component } from 'react';
import api from "../services/api";

import Card from '../components/Card';

import { Grid, Container } from "../styles/global";

class UserList extends Component {

  constructor() {
    super();
    this.state = {
      users: [],
      loading: false,
      errors: null,
    };
  }

  async componentDidMount() {
    this.setState({ loading: true });
    const { data: { data }} = await api.get("/users");
    this.setState({ users: data.users, loading: false });
  }

  render() {
    const { users } = this.state;
    return (
      <Container>
        <Grid>
          {users.map(({ username, email }) => 
            <Card>
              <div className="mdl-card__title">
                <i class="material-icons">face</i>
                {username}
              </div>
              <div className="mdl-card__supporting-text">{email}</div>
            </Card>
          )}
        </Grid>
      </Container>
    );
  }
}

export default UserList;
