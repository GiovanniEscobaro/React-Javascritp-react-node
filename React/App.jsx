// Importamos el hook useState desde la librería de React.
// useState permite crear y manejar estados (variables que cambian con el tiempo).
import { useState } from 'react';

// Definimos el componente principal App
function App() {

  // Creamos una variable de estado llamada 'contador' con valor inicial 0.
  // 'setContador' es la función que usamos para cambiar su valor.
  const [contador, setContador] = useState(0);

  // Lo que retorna el componente se mostrará en la pantalla
  return (
    // Un contenedor centrado con margen arriba
    <div style={{ textAlign: 'center', marginTop: '50px' }}>

      {/* Título principal */}
      <h1>Mi primer contador en React 🚀</h1>

      {/* Mostramos el valor actual del contador */}
      <h2>{contador}</h2>

      {/* Botón que al hacer clic suma 1 al contador */}
      <button onClick={() => setContador(contador + 1)}>
        Sumar +1
      </button>

      {/* Botón que al hacer clic resta 1 al contador.
          Le damos un margen a la izquierda para separarlo del otro botón */}
      <button 
        onClick={() => setContador(contador - 1)} 
        style={{ marginLeft: '10px' }}
      >
        Restar -1
      </button>
    </div>
  );
}

// Exportamos el componente App para que React pueda renderizarlo en pantalla
export default App;
