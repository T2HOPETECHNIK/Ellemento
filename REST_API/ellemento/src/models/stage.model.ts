import {Entity, model, property} from '@loopback/repository';

@model({settings: {strict: false}})
export class Stage extends Entity {
  @property({
    type: 'string',
  })
  stage_name?: string;

  @property({
    type: 'number',
    id: true,
    generated: true,
  })
  stage_id?: number;

  @property({
    type: 'string',
  })
  description?: string;

  // Define well-known properties here

  // Indexer property to allow additional data
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  [prop: string]: any;

  constructor(data?: Partial<Stage>) {
    super(data);
  }
}

export interface StageRelations {
  // describe navigational properties here
}

export type StageWithRelations = Stage & StageRelations;
