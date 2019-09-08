import styled from "styled-components";

export const Body = styled.div`
    .font-sc {
        font-family: 'Source Code Pro', monospace !important;
        font-weight: 600;
    }

    body {
        font-family: 'Roboto', monospace !important;
        font-weight: 400;
        font-size: 16px; 
    }
`;

export const Container = styled.div`
    padding: 20px;
    max-width: 960px;
    margin: 0 auto;
`;

export const Grid = styled.div`
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    grid-gap: 20px;
`;