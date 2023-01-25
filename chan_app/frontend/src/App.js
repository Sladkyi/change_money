import './App.css';
import Header from './modules/Header';
import Content from './modules/Content';
import Footer from './modules/Footer';


function App() {
  return (
    <div className="App">
      <header className="App-header">
         <Header />
         <Content />
         <Footer />
      </header>
    </div>
  );
}



export default App;
