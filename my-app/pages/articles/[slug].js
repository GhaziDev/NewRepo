import axios from 'axios'


export async function getServerSideProps({params}){
    try{
    let res = await axios.get(`http://127.0.0.1:8000/articles/${params.slug}/`)
    let data = res.data
    return {
        props:{data:data}
    }
}
   catch(e){
    return {
        props:{}
    }
   }
}

export default function Component({data}){

    if(data){
        return<div>
            <div>{data.title}</div>
            <div>{data.description}</div>
        </div>
    }

}