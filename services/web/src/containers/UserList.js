import React, { Component } from 'react';
import api from "../services/api";

import Card from '../components/Card';
import Active from '../components/Active';

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
          {users.map(({ id, username, email, active }) => 
            <Card key={id}>
              <div className="mdl-card__title">
                <i className="material-icons">face</i>
                {username}
                <Active isActive={active} />
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
