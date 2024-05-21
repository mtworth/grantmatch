## Inspiration

-As someone in the public sector, I've always found it really difficult to find grants relevant for the projects I'm working on. I thought this would be a great opportunity to try to solve that problem while experimenting with SotA models. 

## What it does

-Matches billions of dollars in federal grants to your project and gives you a verdict on how to fit your project to grant requirements. 

## How we built it

-Embedded thousands of grant descriptions using medium embed model and saved those embeddings. Used HuggingFace. 
-Embed proposed project descriptions on the fly. Used HuggingFace. 
-Use semantic search to score and rank pairings. 
-Evaluate high ranking pairings with gen AI to give a verdict on whether to apply or not. Used Replicate. 

## Challenges we ran into

-Getting data out of grants.gov. No API available, just bulk database downloads. 
-Improving memory usage in Streamlit, solved through use of cache functions in Streamlit and active forums.

## Accomplishments that we're proud of

-Public embedded search for federal grants for the first time ever. 
-Using gen AI as an assistant to the prospective applicant. 

## What we learned

-Open source AI ecosystem is awesome. Lots of high quality options. 
-Streamlit continues to be super fun to use.  

## What's next for Grants Match

I'm planning on iterating on Grants Match by improving on the use of gen AI to better match projects and grants based on eligibility. I also want to continue to iterate on the interface to make the process more "delightful". 
