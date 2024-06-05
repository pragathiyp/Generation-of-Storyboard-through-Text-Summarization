import React from 'react';
import ReactDOM from 'react-dom';
import { ChakraProvider, Box, Heading } from '@chakra-ui/core';

const App = () => {
  return (
    <ChakraProvider>
      <Box textAlign="center" paddingTop="50px">
        <Heading as="h1" size="2xl">PDF to PPT Converter</Heading>
        {/* Add your components here */}
      </Box>
    </ChakraProvider>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));
