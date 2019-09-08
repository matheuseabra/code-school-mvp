import SignUp from './containers/SignUp';
import UsersList from './containers/UserList';

import Sidebar from "./components/Sidebar";
import Header from "./components/Header";

import { Body } from "./styles/global";

const App = () => {
  return (
    <Body className="mdl-layout mdl-js-layout mdl-layout--fixed-header">
      <Header />
      <Sidebar />
      <main className="mdl-layout__content">
        <section className="mdl-layout__tab-panel is-active" id="scroll-tab-1">
          <div className="page-content">
            <SignUp />
          </div>
        </section>
        <section className="mdl-layout__tab-panel" id="scroll-tab-2">
          <div className="page-content">
            <UsersList/>
          </div>
        </section>
      </main>
    </Body>
  );
};

export default App;