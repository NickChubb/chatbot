# EthCommunities (Inactive 🚫)

Communities was a project that I started in an effort to learn and understand Ethereum Smart Contracts (with [Solidity](https://soliditylang.org/)) and interacting with a Blockchain as a decentralized backend service. 

The intention was to be a sort of "Social Network" in which access to community channels (groups) was controlled by holding [ERC-721 (Non-fungible) tokens](https://ethereum.org/en/developers/docs/standards/tokens/erc-721/). The intention of this being that the number of access cards to a group would be limited. Communities can be either public (any user can see posts in the community, but only users with an access token can make posts) or private (only users with an access token can post or view the community).

**🛠️ Tech Stack: JavaScript, React.js, Next.js, MongoDB, Solidity**

### How the backend works

1. Login, community structure and access are managed on a decentralized blockchain network
2. Meta-information about Communities, such as the community image, is hosted on the [Inter Planetary File System (IPFS)](https://ipfs.tech/)
3. Posts in a community are stored on a separate backend database, for example MongoDB

To see the Contracts created for this project, see here: [Contracts](https://github.com/NickChubb/Communities/blob/main/contracts).

## Final Progress

By the time I stopped working on this project, I had implemented several features and have a bare-bones example live on the Sepolia Test Network

### Features Implemented:
- Creating Community Access Tokens
- Public Communities where anyone even without the token can see posts, but only users with an access token can post
- Private Communities where only users with the access token can see posts
- See all current users Communities
- Browse all created Communities
- Upload images for communities to the IPFS
- Upload posts to MongoDB and display on the community page

  
### Photos

#### Explore Communities

<img width="1800" alt="Screenshot 2023-10-15 at 11 46 55 PM" src="https://github.com/NickChubb/Communities/assets/4172020/f8f09c25-d1ef-4478-a04d-575694b8fcdc">

#### Create a new Community

<img width="1800" alt="Screenshot 2023-10-15 at 11 47 45 PM" src="https://github.com/NickChubb/Communities/assets/4172020/0434fae8-f667-4c7b-945f-3015a5c417aa">

#### Community Page

<img width="1800" alt="Screenshot 2023-10-15 at 11 47 24 PM" src="https://github.com/NickChubb/Communities/assets/4172020/6c01b6bc-2665-4937-a526-d32b3c32b78c">

#### User's Page

<img width="1800" alt="Screenshot 2023-10-15 at 11 47 39 PM" src="https://github.com/NickChubb/Communities/assets/4172020/4dfbdb74-779b-4a59-b3f3-5d530b6a8fc3">


## Live Demo

The link for the live demo can be found here: [Communities Testnet Demo](https://communities-mocha.vercel.app)

To access the app, you need a Ethereum browser wallet extension, such as [Metamask](https://metamask.io/), and you will need to have the Sepolia testnet enabled. Since the app is live on an Ethereum testnet, you must use Ether to pay the gas costs of creating and joining communities. Free Sepolia Ether can be obtained from the faucet [here](https://sepoliafaucet.com/). 

[Here is a guide for setting up your Metamask to use Sepolia.](https://medium.com/@razor07/how-to-get-sepolia-eth-from-a-faucet-7420e5ceacb3#:~:text=To%20add%20the%20Sepolia%20testnet%20to%20MetaMask%2C%20click%20the%20network,%E2%80%9CAdd%20a%20network%20manually%E2%80%9D.)
