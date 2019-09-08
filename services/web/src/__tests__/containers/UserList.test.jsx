import React from 'react';
import { mount } from 'enzyme';

import UsersList from '../../containers/UserList';

test('<UsersList />', () => {
    const wrapper = mount(<UsersList />);
    expect(wrapper).toBeTruthy();
});