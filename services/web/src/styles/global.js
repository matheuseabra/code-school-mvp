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
    max-width: 1024px;
    margin: 20px auto;
`;

export const Grid = styled.div`
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
`;

export const FlexCenter = styled.div`
    display: flex;
    align-items: center;
    justify-content: center;
`;